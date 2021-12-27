import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math
from scipy.fft import fft, ifft



tesla_file = open("tesla_share_price.txt", "r")
tesla = []
t = []
counter = 0
for i in tesla_file:
    t.append(counter)
    counter += 1
    tesla.append(np.float(i[:-1]))
tesla_file.close()
################## end setup ##################



################## helper methods ##################
def make_trendline(time, stock):
    trendline = np.polyfit(time, stock, 1)
    m = trendline[0]
    c = trendline[1]
    y = []
    
    for i in range(len(t)):
        # y = m*t + c
        y.append(m*i + c)

    return y

def LPF_filter():
    global tesla, t
    LPF_array = []

    f_sample = 40000 # sampling frequency
    f_pass = 4000  # pass band frequency
    f_stop = 8000  # stop band frequency
    fs = 0.5
    wp = f_pass/(f_sample/2)  # pass band freq in radian
    ws = f_stop/(f_sample/2) # stop band freq in radian
    Td = 1  # Sampling Time
    g_pass = 0.5 # pass band ripple
    g_stop = 40 # stop band attenuation

    omega_p = (2/Td)*np.tan(wp/2)
    omega_s = (2/Td)*np.tan(ws/2)
    N, Wn = signal.buttord(omega_p, omega_s, g_pass, g_stop, analog=True) # Design of Filter using signal.buttord function
    
    print("Order of the Filter=", N)  # N is the order
    print("Cut-off frequency= {:.3f} rad/s ".format(Wn)) # Wn is the cut-off freq of the filter
    
    ###### Conversion in Z-domain ######
    b, a = signal.butter(N, Wn, 'low', True) # b is the numerator of the filter & a is the denominator
    z, p = signal.bilinear(b, a, fs)
    w, h = signal.freqz(z, p, 512) # w is the freq in z-domain & h is the magnitude in z-domain

    plt.semilogx(w, 20*np.log10(abs(h)))
    plt.xscale('log')
    plt.title('Butterworth filter frequency response')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(100, color='green')
    plt.show()

    # Impulse Response
    imp = signal.unit_impulse(40)
    c, d = signal.butter(N, 0.5)
    response = signal.lfilter(c, d, imp)
    
    plt.stem(np.arange(0, 40), imp, use_line_collection=True)
    plt.stem(np.arange(0, 40), response, use_line_collection=True)
    plt.margins(0, 0.1)
    
    plt.xlabel('Time [samples]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    fig, ax1 = plt.subplots()
    ax1.set_title('Digital filter frequency response')
    ax1.set_ylabel('Angle(radians)', color='g')
    ax1.set_xlabel('Frequency [Hz]')
    angles = np.unwrap(np.angle(h))
    ax1.plot(w/2*np.pi, angles, 'g')
    ax1.grid()
    ax1.axis('tight')
    plt.show()




    return LPF_array


def fft_method():
    global tesla, t
    fft_array = []


    return fft_array


def correlation():
    # correlate using np.corrcoef(np_array1, np_array2)
    return

def support():
    # add code that identifies and marks out supports
    return

################## end helper methods ##################


################## plots ##################
# plt.plot(t, tesla)
# plt.title('TSLA')
# plt.ylabel('Stock Price (USD)')
# plt.xlabel('Days')

# trendline = make_trendline(t, tesla)
# plt.plot(t, trendline)
# plt.show()
# ###

LPF_filter()

# N = 1000
# # T = 1/800
# yf = fft(tesla)
# xf = fftfreq(N, T)[:N//2]

# plt.plot()



# plt.show()



