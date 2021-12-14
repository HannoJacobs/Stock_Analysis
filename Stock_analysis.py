import yfinance as yf
import matplotlib.pyplot as plt

# tesla = yf.Ticker("TSLA")
# dictionary = tesla.info
# price = dictionary['currentPrice']
# print ("\n", price, "\n")

from datetime import datetime
now = datetime.today().strftime('%Y-%m-%d')
print("date now = ", now)
tesla_price_chart = yf.download('tsla','2020-01-01', now)
bitcoin_price_chart = yf.download('BTC-USD','2020-01-01', now)

fig, ax = plt.subplots(2, sharex=True)
ax[0].set_title('TSLA')
ax[0].plot(tesla_price_chart['Adj Close'])
ax[1].set_title('Bitcoin')
ax[1].plot(bitcoin_price_chart['Adj Close'])



plt.show()