import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
import math
from scipy.fft import fft, ifft


tesla_file = open("tesla_share_price.txt", "r")
rough_tesla_array = []
t = []
counter = 0
num_data_points = 0
for i in tesla_file:
    rough_tesla_array.append(np.float(i[:-1]))
    num_data_points += 1
tesla_file.close()

substring = 1 # change this to take the last x part of 2 years
number_of_points = round(num_data_points/substring)
start = num_data_points - number_of_points
end = num_data_points
tesla = []
for i in range(start, end):
    t.append(counter)
    counter += 1
    tesla.append(rough_tesla_array[i])


moving_average10pt = []
moving_average20pt = []
moving_average30pt = []
moving_average40pt = []
moving_average50pt = []


################## end setup ##################



################## helper methods ##################
def calc_trendline(time, stock):
    global tesla, t, counter
    trendline = np.polyfit(time, stock, 1)
    m = trendline[0]
    c = trendline[1]
    y = []
    
    for i in range(len(t)):
        # y = m*t + c
        y.append(m*i + c)

    return y

def plot_trendline(time, stock):
    global tesla, t, counter
    trendline = np.polyfit(time, stock, 1)
    m = trendline[0]
    c = trendline[1]
    y = []
    
    for i in range(len(t)):
        # y = m*t + c
        y.append(m*i + c)

    plt.plot(t, tesla, 'k', linewidth=3, label='Daily closing stock price')
    plt.title('TSLA')
    plt.ylabel('Stock Price (USD)')
    plt.xlabel('Days')

    # trendline = make_trendline(t, tesla)
    plt.plot(t, y, linewidth=0.5, label='First order linear trendline')

    return y

def kite_LPF():
    global tesla, t, counter
    kite_LPF_array = []
    
    order = 1
    multiplier = 10
    # sampling_freq = 2*counter
    sampling_freq = multiplier * counter
    cutoff_freq = sampling_freq/60
    # sampling_duration = 5
    # number_of_samples = sampling_freq * sampling_duration
    offset = 0
    sampling_duration = counter
    number_of_samples = counter


    time = np.linspace(0, sampling_duration, number_of_samples, endpoint=False)
    # signal = np.sin(2*np.pi*time) + 0.5*np.cos(6*2*np.pi*time) + 1.5*np.sin(9*2*np.pi*time)
    signal = tesla

    normalized_cutoff_freq = 2 * cutoff_freq / sampling_freq
    numerator_coeffs, denominator_coeffs = scipy.signal.butter(order, normalized_cutoff_freq)

    # filtered_signal = scipy.signal.lfilter(numerator_coeffs, denominator_coeffs, signal)
    filtered_signal = scipy.signal.lfilter(numerator_coeffs, denominator_coeffs, signal)

    # plt.plot(time, signal, 'b-', label='current stock price')
    plt.plot((time - offset), filtered_signal, 'g-', linewidth=2, label='LPF stock price')
    plt.legend()


    
    return kite_LPF_array

def plot_moving_average(gaps):
    global tesla, t, counter
    tesla_array = np.array(tesla)

    avg_array = []
    for i in range(gaps):#causal
        causal = "causal"
        avg_array.append(0)

    for i in range(gaps, counter):
        index1 = i-gaps
        index2 = i

        avg = ( np.sum(tesla_array[index1:index2]) )/gaps
        avg_array.append(avg)
    
    # for i in range(gaps):#non-causal
    #     causal = "non-causal"
    #     avg_array.append(0)


    text = "{num:d} point {txt} moving average"
    plt.plot(t, avg_array, label=text.format(num = gaps, txt = causal))
    plt.legend()


    return

def calc_moving_average(gaps):
    global tesla, t, counter
    tesla_array = np.array(tesla)

    avg_array = []
    for i in range(gaps):#causal
        causal = "causal"
        avg_array.append(0)

    for i in range(gaps, counter):
        index1 = i-gaps
        index2 = i

        avg = ( np.sum(tesla_array[index1:index2]) )/gaps
        avg_array.append(avg)
    

    return avg_array

def fft_method(data):
    global tesla, t, counter
    
    freq = counter
    N_fft = counter*1
    f_1 = np.arange(0, freq, freq/N_fft)
    Y_r = np.fft.fft(data, N_fft)/N_fft # was like this
    Y_shifted = np.fft.fftshift(Y_r)
    Y_r_mag = 10*np.log10(np.abs(Y_shifted))
    plt.plot(f_1,Y_r_mag)
    plt.plot(f_1, Y_r_mag, label="FFT Method")

    plt.legend()
    plt.grid()

    return Y_r_mag

def correlation():
    global tesla, t, counter
    trendline = calc_trendline(t, tesla)
    # correlate using np.corrcoef(np_array1, np_array2)

    corr = np.corrcoef(trendline, tesla)[0,1]
    print("\n" + str(corr) + "\n")
    return corr

def support():
    global tesla, t, counter
    # add code that identifies and marks out supports
    return

################## end helper methods ##################


################## plots ##################
trendline = plot_trendline(t, tesla)
# kite_LPF()
plot_moving_average(10)
plot_moving_average(20)
plot_moving_average(30)
plot_moving_average(50)


# fft_method(calc_moving_average(1))
# fft_method(calc_moving_average(10))
# fft_method(calc_moving_average(100))

correlation()





plt.show()