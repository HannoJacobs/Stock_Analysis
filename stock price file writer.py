import yfinance as yf

tesla_price_chart = yf.download('tsla', period="2y")
tesla_file = open("tesla_share_price.txt", "w")

for i in range(len(tesla_price_chart)):
    val = tesla_price_chart['Adj Close'][i]
    tesla_file.write(str(val)+"\n")

tesla_file.close()