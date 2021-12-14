import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from datetime import datetime
start = '2020-01-01'
end = datetime.today().strftime('%Y-%m-%d') # works

# tesla = yf.Ticker("TSLA")
# dictionary = tesla.info
# price = dictionary['currentPrice']
# print ("\n", price, "\n")



def plot_the_data():
    # global tesla_price_chart, bitcoin_price_chart

    tesla_price_chart = yf.download('tsla','2020-01-01', end)
    bitcoin_price_chart = yf.download('BTC-USD','2020-01-01', end)

    ####################### plots #######################
    fig, ax = plt.subplots(2, sharex=True)
    ax[0].set_title('TSLA')
    ax[0].set_ylabel('USD ($)')
    y = tesla_price_chart['Adj Close']
    # trendline1 = np.polyfit(int_date, y, 1)
    ax[0].plot(y)
    ##################

    ax[1].set_title('Bitcoin')
    ax[1].set_ylabel('USD ($)')
    y = bitcoin_price_chart['Adj Close']
    ax[1].plot(y)


    plt.show()
    return



plot_the_data()




