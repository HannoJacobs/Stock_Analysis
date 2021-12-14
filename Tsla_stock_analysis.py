import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

tesla_price_chart = yf.download('tsla', period="2y")
t = []
tesla = []

for i in range(len(tesla_price_chart)):
    t.append(i)
    tesla.append(tesla_price_chart['Adj Close'][i])


################## helper methods ##################
def make_trendline_data_order_1(trendline):
    m = trendline[0]
    c = trendline[1]
    y = []
    
    for i in range(len(t)):
        # y = m*t + c
        y.append(m*i + c)

    return y

def make_trendline_data_order_x(trendline, order = 5):
    global tesla, btc, t
    y = []
    
    # trendline1_x = np.polyfit(t, tesla, order)

    # x2 = trendline[0]
    # x1 = trendline[1]
    # x0 = trendline[2]

    # y = []
    # for i in range(len(t)):
    #     # y = x0*i^2 + x1*i + x0
    #     y.append(x0*(i**2) + x1*i + x0)

    return y

def moving_average(days = 10):
    global tesla, btc, t
    moving_average = []


    return moving_average

def fft_method():
    global tesla, btc, t
    fft_array = []


    return fft_array

def LPF_filter():
    global tesla, btc, t
    LPF_array = []


    return LPF_array

################## end helper methods ##################



################## plots ##################
fig, ax = plt.subplots(2, sharex=True)
##################
plt.set_title('TSLA')
plt.set_ylabel('USD ($)')
plt.plot(t, tesla)

trendline1_1 = np.polyfit(t, tesla, 1)
trend_line_array_1_1 = make_trendline_data_order_1(trendline1_1)
plt.plot(t, trend_line_array_1_1)

# trend_line_array_1_x = make_trendline_data_order_x(trendline1_x, 5)
# ax[0].plot(t, trend_line_array_1_x)

plt.show()

