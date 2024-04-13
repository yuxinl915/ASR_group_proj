import numpy as np
import pandas as pd
import scipy.signal
import matplotlib.pyplot as plt


## Feature extraction functions

# Integrated EMG (IEMG), Mean Absolute (MAV)
def get_iemg_mav(data):
    iemg = np.sum(np.abs(data), axis=1)
    mav = np.mean(np.abs(data), axis=1)
    return iemg, mav

# Simple Square Integral (SSI)
def get_ssi(data):
    ssi = np.sum(data**2, axis=1)
    return ssi

# Frequency Median (FMD)
def get_fmd(f, psd, fmn):
    numerator = np.sum(psd * (f - fmn)**2)
    fmd = np.sqrt(numerator / np.sum(psd))
    return fmd

# Frequency Mean (FMN)
def get_fmn_trial(f, psd):
    fmn_trial = []
    for ch in range(len(psd)):
        ch_data = psd[ch,:]
        fmn = sum(f * ch_data) / sum(ch_data)
        fmn_trial.append(fmn)
    return fmn_trial

# ------------------------------------------------------------------------------------------

## Read data file, apply filter, extract feature

def read_emg_data(file_path):
    # Assuming the file is a CSV with a header and timepoints are rows
    data = pd.read_csv(file_path, usecols=list(range(2, 10)), skiprows=49)
    return data

def preprocess_emg(data, fs=1000, lowcut=20, highcut=450):
    # Bandpass filter settings
    nyq = 0.5 * fs  # Nyquist Frequency
    low = lowcut / nyq
    high = highcut / nyq
    b, a = scipy.signal.butter(4, [low, high], btype='band')
    
    # Apply filter
    filtered_data = scipy.signal.filtfilt(b, a, data, axis=0)
    return filtered_data

def extract_features(data):
    # Assuming data is already preprocessed and shaped correctly
    # Calculate PSD for frequency domain features
    f, psd = scipy.signal.welch(data, fs=1000, nperseg=256)
    fmn = get_fmn_trial(f, psd)
    
    # Time-domain features
    iemg, mav = get_iemg_mav(data)
    ssi = get_ssi(data)
    var = np.var(data, axis=1)
    rms = np.sqrt(np.mean(data**2, axis=1))
    
    # Frequency domain features
    fmd = np.array([get_fmd(f, psd[ch, :], fmn[ch]) for ch in range(len(psd))])
    
    return iemg, mav, ssi, fmd, fmn, var, rms

# ------------------------------------------------------------------------------------------

# Run file
if __name__ == '__main__':
    file_path = 'dataset/s10_r_1/s10_r_1-paper-0-emg.csv'
    raw_data = read_emg_data(file_path)
    filtered_data = preprocess_emg(raw_data.values)
    features = extract_features(filtered_data.T)  # Transpose if necessary based on your reshaping needs

    print("Features: ", type(features), len(features))
    print('\n')
    print("IEMG: ", len(features[0]))
    print("IEMG: ", features[0])
    print('\n')
    print("MAV: ", len(features[1]))
    print("MAV: ", features[1])
    print('\n')
    print("SSI: ", len(features[2]))
    print("SSI: ", features[2])
    print('\n')
    print("FMD: ", len(features[3]))
    print("FMD: ", features[3])
    print('\n')
    print("FMN: ", len(features[4]))
    print("FMN: ", features[4])
    print('\n')
    print("VAR: ", len(features[5]))
    print("VAR: ", features[5])
    print('\n')
    print("RMS: ", len(features[6]))
    print("RMS: ", features[6])
    print('\n')


