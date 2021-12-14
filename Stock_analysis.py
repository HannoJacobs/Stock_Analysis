import yfinance as yf

tesla = yf.Ticker("TSLA")
dictionary = tesla.info
price = dictionary['currentPrice']
print ("\n", price, "\n")
