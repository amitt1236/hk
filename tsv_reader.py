from torch.utils.data import Dataset
import torch.nn.functional as F
import pandas as pd
import numpy as np
import torch

class CustomDataset(Dataset):
    def __init__(self, file):
        self.df = pd.read_csv(file, sep='\t', header=None)
        self.df = self.df.drop(self.df[self.df.iloc[:, 4] == -1].index)

        self.lst = list(set(self.df.iloc[:, 1]))

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, idx):
        channels_df = self.df[self.df.iloc[:, 1] == self.lst[idx]]
        
        # Vectorized operation to convert the string elements into integers
        array = channels_df.iloc[:, 6].str.split(",").apply(lambda x: np.array(x))

        numpy_array = np.vstack(array.to_numpy())
        padded =  F.pad(input=torch.tensor(numpy_array.astype(np.float32)), pad=(0, 612-numpy_array.shape[1]), mode='constant', value=0) 
        return padded, torch.tensor(int(channels_df.iloc[-1, 4]))


if __name__ == "__main__":
    # dataset = CustomDataset('/Users/amitaflalo/Downloads/MU.txt')
    dataset = CustomDataset('/Users/amitaflalo/Desktop/hk/MU_processed.txt')

    for i in range(1000):
        arr, label = dataset[i]
        print(label)
    