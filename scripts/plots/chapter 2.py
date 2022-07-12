import sys
sys.path.append("../..") # adds higher directory to python modules path
from src.pypm import metrics, data_io
import matplotlib.pyplot as plt

awu = data_io.load_eod_data('AWU')
bmg = data_io.load_eod_data('BMG')
cuu = data_io.load_eod_data('CUU')


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


#  Figure 2.1:

# stonks = {"AWU": awu["close"],
#           "BMG": bmg["close"],
#           "CUU": cuu["close"]}
# plot_function(stonks)



# plt.plot(awu["close"], label="AWU")
# plt.plot(bmg["close"], label="BMG")
# plt.plot(cuu["close"], label="CUU")
# plt.legend()
# plt.xlabel("date")
# plt.ylabel("price ($'s)")
# plt.gcf().autofmt_xdate()
# plt.grid()
# plt.show()


#  Figure 2.2:

# stonks = {"AWU, BMG, CUU Portfolio": (awu["close"] + bmg["close"] + cuu["close"])/3}
# plot_function(stonks)


#  Figure 2.3:

# not sure how the correct graph looks...
# cash = awu["close"][:]
#
# cash[:"2015-01-01"] = 75
# cash["2015-01-01":] = 25
#
# stonks = {"Portfolio": (awu["close"] + bmg["close"] + cuu["close"])/3,
#           "Equity curve": cash + (awu["close"] + bmg["close"] + cuu["close"])/3 - 0.3/5,
#           "Cash": cash}
#
# plot_function(stonks)



#  Figure 2.4:

from src.pypm import metrics
r_ser = metrics.calculate_return_series(awu["close"])

ser = {"Return series": r_ser}

# plot_function(ser, y_lab="returns (%)")



#  Figure 2.5:

r_ser_log = metrics.calculate_log_return_series(awu["close"])

ser = {"Log return series": r_ser_log}

# plot_function(ser, y_lab="log returns")


#  Figure 2.6:

r_ser = metrics.calculate_return_series(awu["close"])
r_ser_log = metrics.calculate_log_return_series(awu["close"])
# fig, (ax1, ax2) = plt.subplots(1, 2)
# ax1.set_title("Log returns")
# ax1.hist(r_ser_log, bins=70)
# ax1.set_ylabel('frequency')
#
# ax2.set_title("Percent returns")
# ax2.hist(r_ser, bins=70)
# plt.show()



#  Figure 2.7: Still don't get teh standardized price on y-axis

r_ser_log = metrics.calculate_log_return_series(awu["close"])
awu_vol = metrics.calculate_annualized_volatility(r_ser_log)
r_ser_log = metrics.calculate_log_return_series(bmg["close"])
bmg_vol = metrics.calculate_annualized_volatility(r_ser_log)
r_ser_log = metrics.calculate_log_return_series(cuu["close"])
cuu_vol = metrics.calculate_annualized_volatility(r_ser_log)


stonks = {f"AWU: {round(awu_vol, 3)}": awu["close"],
          f"BMG: {round(bmg_vol, 3)}": bmg["close"],
          f"CUU: {round(cuu_vol, 3)}": cuu["close"]}
plot_function(stonks)




