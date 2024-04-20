import numpy as np
import scipy.signal as sps
import utils
from scipy.io import wavfile


if __name__ == '__main__':
    lpc_rate = 8000

    # Reading signal
    args = utils.parse_to_code()
    sampling_rate, data = wavfile.read(args.path)

    # Resampling
    num_samples = round(len(data) * lpc_rate / sampling_rate)
    data = sps.resample(data, num_samples)

    # Flattening
    data = np.mean(data, axis=1)

    # Pre-emphasis
    x = np.copy(data)
    x[1:] = data[:-1] - 0.9375*data[1:]
