import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

tesla_price_chart = yf.download('tsla', period="2y")
tesla = tesla_price_chart['Adj Close']
print (len(tesla))


def moving_average(days = 10):
    global tesla, btc
    


    return










################## plots ##################
fig, ax = plt.subplots(2, sharex=True)
##################
ax[0].set_title('TSLA')
ax[0].set_ylabel('USD ($)')
# trendline1 = np.polyfit(int_date, y, 1)
ax[0].plot(tesla)
##################
# ax[1].set_title('Bitcoin')
# ax[1].set_ylabel('USD ($)')
# ax[1].plot(t, btc)

# ax[0].grid()
# ax[1].grid()
plt.show()