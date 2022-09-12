import pandas as pd
import sys
sys.path.append("../..") # adds higher directory to python modules path
from src.pypm import data_io, portfolio
import matplotlib.pyplot as plt

symbol = 'AWU'
df = data_io.load_eod_data(symbol)
shares_to_buy = 50


def plot_function(series_dict: dict, x_lab: str="date", y_lab: str="price"):
    """
    Args:
        series_dict (dict): dictionary of data series, where key is the label name.
    """

    for d in series_dict:
        plt.plot(series_dict[d], label=d)

    plt.legend()
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.show()


for i, row in enumerate(df.itertuples()):
	date = row.Index
	price = row.close

	if i == 123:
		position = portfolio.Position(symbol, date, price, shares_to_buy)
	elif 123 < i < 234:
		position.record_price_update(date, price)
	elif i == 234:
		position.exit(date, price)

position.print_position_summary()

stonks = {"AWU": df["close"][:"2011"],
          "Position": position.price_series}
plot_function(stonks)



# Returns ...
# AWU       Trade summary
# Date:     Wed Jun 30, 2010 -> Tue Dec 07, 2010 [111 days]
# Price:    $220.34 -> $305.98 [38.9%]
# Value:    $11017.0 -> $15299.0 [$4282.0]