from torch.utils.data import DataLoader
from tsv_reader import CustomDataset
from model import LSTMeeg
from tqdm import tqdm
import torch
from torch import nn 

def train(model, opt, loader, device, epoch):
    count = 0
    cre = nn.CrossEntropyLoss()
    for _  in tqdm(range(epoch)):
        total_loss = 0
        for batch in loader:
            eeg, label = batch
            eeg.to(device)
            label.to(device)
            count = count + 1
            opt.zero_grad()
            
            pred = model(eeg)
            loss = cre(pred, label)

            loss.backward()
            opt.step()
            total_loss = total_loss + loss

            print(loss)
        
        print(total_loss / len(loader))

if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # load data
    dataset = CustomDataset('/Users/amitaflalo/Desktop/hk/MU_processed.txt')
    loader = DataLoader(dataset, batch_size=36, shuffle=True)

    model = LSTMeeg(4, 256, 10)
    opt = torch.optim.AdamW(model.parameters(), lr=0.0001)
    train(model, opt, loader, device, 50)

