import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.dates import AutoDateLocator, AutoDateFormatter, date2num, mdates
from matplotlib.dates import AutoDateLocator, AutoDateFormatter, date2num
from matplotlib import pylab
import dateutil
# tesla = yf.Ticker("TSLA")
# dictionary = tesla.info
# price = dictionary['currentPrice']
# print ("\n", price, "\n")

from datetime import datetime
now = datetime.today().strftime('%Y-%m-%d')
# start = np.datetime64('2020-01-01')
# end = np.datetime64(now)
start = '2020-01-01'
end = now
date_datetime = datetime.strptime(start, '%Y-%m-%d')
t = pd.date_range(start, end, periods=200).to_pydatetime()
int_date = date2num(t)

# t = np.linspace(start.value, end.value, 100)
# t = np.linspace(start, end, 100)
# t = pd.to_datetime(t)
# t = pd.to_datetime(start, end)
tesla_price_chart = yf.download('tsla','2020-01-01', now)
bitcoin_price_chart = yf.download('BTC-USD','2020-01-01', now)


####################### plots ###################################
fig, ax = plt.subplots(2, sharex=True)
ax[0].set_title('TSLA')
ax[0].set_ylabel('USD ($)')
y = tesla_price_chart['Adj Close']
dates = [dateutil.parser.parse(x) for x in t]
x = mdates.date2num(dates)

trendline1 = np.polyfit(int_date, y, 1)




ax[0].plot(y)
################################################################
################################################################
ax[1].set_title('Bitcoin')
ax[1].set_ylabel('USD ($)')


y = bitcoin_price_chart['Adj Close']
ax[1].plot(y)
################################################################


plt.show()