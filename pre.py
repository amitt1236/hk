import pandas as pd
import numpy as np
from scipy import signal
import pywt
from tqdm import tqdm

def butter_highpass_filter(data, cutoff, order, fs):
    b, a = butter_highpass(cutoff, fs, order=order)
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data


def butter_highpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a


def notch_filter(data, freq, fs):
    notch_freqs = np.arange(freq, fs / 2, freq)
    filtered_data = data
    for f in notch_freqs:
        filtered_data = notch_single(filtered_data, f, fs)
    return filtered_data


def notch_single(data, freq, fs):
    nyquist = 0.5 * fs
    q = 30.0  # Quality factor
    w0 = freq / nyquist
    b, a = signal.iirnotch(w0, q)
    filtered_data = signal.lfilter(b, a, data)
    return filtered_data


df = pd.read_csv("/Users/amitaflalo/Downloads/MU.txt", sep='\t', header=None)
print(len(df))

for i in tqdm(range(len(df))):
    x = df.iloc[i, 6]
    eeg_data = np.array(x.split(','), dtype=np.float64)

    # Butterworth high-pass filter of order 5 at 0.1 Hz
    cutoff_freq = 0.1
    order = 5
    sampling_rate = 220
    highpass_filtered_data = butter_highpass_filter(eeg_data, cutoff_freq, order, sampling_rate)

    # Notch filter to eliminate the 60 Hz electrical environmental noise
    notch_freq = 60
    notch_filtered_data = notch_filter(highpass_filtered_data, notch_freq, sampling_rate)

    # DWT using the Daubechies-4 wavelet with three-level decomposition
    wavelet = 'db4'
    decomposition_level = 2
    decomposed_coeffs = pywt.wavedec(notch_filtered_data, wavelet, level=decomposition_level)

    # Signal decomposition: the signal is decomposed into approximation coefficients (representing the lower frequency sub-band)
    # and detail coefficients (representing the higher frequency sub-band)
    approx_coeffs = decomposed_coeffs[0]
    detail_coeffs = decomposed_coeffs[1:]

    # Taking only the detail coefficients as the feature vector
    feature_vector = np.concatenate(detail_coeffs)

    # Inverse Reconstruction
    reconstructed_signal = pywt.waverec(decomposed_coeffs, wavelet)

    # Data Standardization (Z-score normalization)
    mean = np.mean(eeg_data)
    std = np.std(eeg_data)
    standardized_data = (eeg_data - mean) / std

    # Min-Max Scaling
    min_val = np.min(standardized_data)
    max_val = np.max(standardized_data)
    scaled_data = (standardized_data - min_val) / (max_val - min_val)
    lst = [str(num) for num in scaled_data]
    df.iloc[i, 6] = ','.join(lst)

df.to_csv("MU_processed.txt", sep='\t', header=None, index=None)
