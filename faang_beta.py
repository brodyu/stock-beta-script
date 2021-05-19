import yfinance as yf
from scipy import stats

# Class for calculating faang stock's beta
class FaangBeta:
    # Initialize ticker, start_date, and end_date values
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def get_historical(self):
        # Take in ticker and index
        symbols = [self.ticker, '^GSPC']
        # API call to pull historical pricing data
        data = yf.download(symbols, self.start_date, self.end_date)['Adj Close']
        # Check for any null values and exit program if they exist
        if data.isnull().values.any() == True:
            print("Null values exist, exiting program")
            exit()
        # Return dataframe
        return data

    def calculate_beta(self):
        # Call yfinance API to pull data
        data = self.get_historical()
        # Gather percent change for the stock and index and eliminate first NA row
        x = data[data.columns[0]].pct_change()[1:]
        y = data[data.columns[1]].pct_change()[1:]
        # Find the line of best fit that minimizes the sum of the square errors
        slope, intercept, r, p, std_err = stats.linregress(y, x)
        # Return the beta coefficient which is the slope of the line of best fit
        return slope
        

# Main method    
if __name__ == "__main__":
    # Pull FAANG Beta Coefficients
    # start_date and end_date must follow 'YYYY-MM-DD' format
    symbols = ["FB", "AAPL", "AMZN", "NFLX", "GOOG"]
    for symbol in symbols:
        stock = FaangBeta(symbol, '2016-05-19', '2021-05-19')
        print(symbol, "beta :", stock.calculate_beta())

    # Other use case: 
    # fb = FaangBeta("FB", '2016-01-01', '2021-01-01').calculate_beta()
    # print('FB Beta: ', fb)