import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
start = '2020-01-01'
end = datetime.today().strftime('%Y-%m-%d') # works

tesla_price_chart = yf.download('tsla','2020-01-01', end)
bitcoin_price_chart = yf.download('BTC-USD','2020-01-01', end)
tesla = tesla_price_chart['Adj Close']
btc = bitcoin_price_chart['Adj Close']
numdays = len(tesla)
print ("numdays = ", numdays)
# t = np.linspace(0, numdays, 1)
t = np.linspace(0, numdays, 1)
print ("t = ", t)


# tesla = yf.Ticker("TSLA")
# dictionary = tesla.info
# price = dictionary['currentPrice']
# print ("\n", price, "\n")

def moving_average(days = 10):
    global tesla, btc
    


    return










################## plots ##################
fig, ax = plt.subplots(2, sharex=True)
##################
ax[0].set_title('TSLA')
ax[0].set_ylabel('USD ($)')
# trendline1 = np.polyfit(int_date, y, 1)
ax[0].plot(t, tesla)
##################
ax[1].set_title('Bitcoin')
ax[1].set_ylabel('USD ($)')
ax[1].plot(t, btc)

ax[0].grid()
ax[1].grid()
plt.show()