import matplotlib.pyplot as plt
import numpy as np
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


def fft_method():
    global tesla, t
    fft_array = []


    return fft_array

def LPF_filter():
    global tesla, t
    LPF_array = []


    return LPF_array

def correlation():
    # crorelate using np.corrcoeff(np_array1, np_array2)
    return

################## end helper methods ##################


################## plots ##################
plt.plot(t, tesla)
plt.title('TSLA')
plt.ylabel('Stock Price (USD)')
plt.xlabel('Days')

trendline = make_trendline(t, tesla)
plt.plot(t, trendline)
plt.show()
###


N = 1000
# T = 1/800
yf = fft(tesla)
xf = fftfreq(N, T)[:N//2]

plt.plot()



# plt.show()



