import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
start = '2020-01-01'
end = datetime.today().strftime('%Y-%m-%d') # works

tesla_price_chart = yf.download('tsla','2020-01-01', end)
bitcoin_price_chart = yf.download('BTC-USD','2020-01-01', end)
tesla = tesla_price_chart['Adj Close']
btc = bitcoin_price_chart['Adj Close']

# tesla = yf.Ticker("TSLA")
# dictionary = tesla.info
# price = dictionary['currentPrice']
# print ("\n", price, "\n")











################## plots ##################
fig, ax = plt.subplots(2, sharex=True)
##################
ax[0].set_title('TSLA')
ax[0].set_ylabel('USD ($)')
# trendline1 = np.polyfit(int_date, y, 1)
ax[0].plot(tesla)
##################
ax[1].set_title('Bitcoin')
ax[1].set_ylabel('USD ($)')
ax[1].plot(btc)

ax[0].grid()
ax[1].grid()
plt.show()