import yfinance as yf
from scipy import stats

# class for calculating faang stock's beta
class FaangBeta:
    # constructor 
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def beta(self):
        symbols = [self.ticker, '^GSPC']
        # API call to pull historical pricing data
        data = yf.download(symbols, self.start_date, self.end_date)['Adj Close']
        # check for any null values and exit program if they exist
        if data.isnull().values.any() == True:
            print("Null values exist, exiting program")
            exit()
        # gather percent change for the stock and index and eliminate first NA row
        x = data[data.columns[0]].pct_change()[1:]
        y = data[data.columns[1]].pct_change()[1:]
        # find the line of best fit that minimizes the sum of the square errors
        slope, intercept, r, p, std_err = stats.linregress(y, x)
        # return the beta coefficient which is the slope of the line of best fit
        return slope
        

    
if __name__ == "__main__":
    # FAANG Beta Coefficients
    fb = FaangBeta("FB", '2016-01-01', '2021-01-01').beta()
    aapl = FaangBeta("AAPL", '2016-01-01', '2021-01-01').beta()
    amzn = FaangBeta("AMZN", '2016-01-01', '2021-01-01').beta()
    nflx = FaangBeta("NFLX", '2016-01-01', '2021-01-01').beta()
    googl = FaangBeta("GOOGL", '2016-01-01', '2021-01-01').beta()

    print('FB Beta: ', fb)
    print('AAPL Beta: ', aapl)
    print('AMZN Beta: ', amzn)
    print('NFLX Beta: ', nflx)
    print('GOOGL Beta: ', googl)
