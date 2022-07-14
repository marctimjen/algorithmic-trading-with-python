import sys
sys.path.append("../..") # adds higher directory to python modules path
from src.pypm import metrics, data_io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

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



#  Figure 2.7:

# r_ser_log = metrics.calculate_log_return_series(awu["close"])
# awu_vol = metrics.calculate_annualized_volatility(r_ser_log)
# r_ser_log = metrics.calculate_log_return_series(bmg["close"])
# bmg_vol = metrics.calculate_annualized_volatility(r_ser_log)
# r_ser_log = metrics.calculate_log_return_series(cuu["close"])
# cuu_vol = metrics.calculate_annualized_volatility(r_ser_log)
#
# # standardize so that you start by investing 100 dollar in each stock:
# stonks = {f"AWU: {round(awu_vol, 3)}": 100*awu["close"]/awu["close"][0],
#           f"BMG: {round(bmg_vol, 3)}": 100*bmg["close"]/bmg["close"][0],
#           f"CUU: {round(cuu_vol, 3)}": 100*cuu["close"]/cuu["close"][0]}
# plot_function(stonks, y_lab="Standardized price ($'s)")
#




#  Figure 2.8:

# awu_vol = metrics.calculate_sharpe_ratio(awu["close"])
# bmg_vol = metrics.calculate_sharpe_ratio(bmg["close"])
# cuu_vol = metrics.calculate_sharpe_ratio(cuu["close"])
#
#
# stonks = {f"AWU: {round(awu_vol, 3)}": 100*awu["close"]/awu["close"][0],
#           f"BMG: {round(bmg_vol, 3)}": 100*bmg["close"]/bmg["close"][0],
#           f"CUU: {round(cuu_vol, 3)}": 100*cuu["close"]/cuu["close"][0]}
# plot_function(stonks, y_lab="Standardized price ($'s)")




#  Figure 2.9:


# r_ser_log = metrics.calculate_return_series(awu["close"])
# awu_vol = metrics.calculate_annualized_downside_deviation(r_ser_log)
# r_ser_log = metrics.calculate_return_series(bmg["close"])
# bmg_vol = metrics.calculate_annualized_downside_deviation(r_ser_log)
# r_ser_log = metrics.calculate_return_series(cuu["close"])
# cuu_vol = metrics.calculate_annualized_downside_deviation(r_ser_log)
#
#
# stonks = {f"AWU: {round(awu_vol, 3)}": 100*awu["close"]/awu["close"][0],
#           f"BMG: {round(bmg_vol, 3)}": 100*bmg["close"]/bmg["close"][0],
#           f"CUU: {round(cuu_vol, 3)}": 100*cuu["close"]/cuu["close"][0]}
# plot_function(stonks, y_lab="Standardized price ($'s)")



#  Figure 2.10:
#
# awu_vol = metrics.calculate_sortino_ratio(awu["close"])
# bmg_vol = metrics.calculate_sortino_ratio(bmg["close"])
# cuu_vol = metrics.calculate_sortino_ratio(cuu["close"])
#
#
# stonks = {f"AWU: {round(awu_vol, 3)}": 100*awu["close"]/awu["close"][0],
#           f"BMG: {round(bmg_vol, 3)}": 100*bmg["close"]/bmg["close"][0],
#           f"CUU: {round(cuu_vol, 3)}": 100*cuu["close"]/cuu["close"][0]}
# plot_function(stonks, y_lab="Standardized price ($'s)")



#  Figure 2.11:
#
# awu_draw = metrics.calculate_drawdown_series(awu["close"], method="dollar")
#
#
# ze = awu["close"][:].copy()
# ze[:] = 0
#
# stonks = {f"AWU": awu["close"],
#           "Cumulative max": awu["close"].cummax(),
#           "Drawdown": awu_draw,
#           "Zero": ze
#           }
#
# plot_function(stonks)



#  Figure 2.12:

# awu_max_draw = metrics.calculate_max_drawdown_with_metadata(awu["close"], method="dollar")
# awu_max_draw_log = metrics.calculate_max_drawdown_with_metadata(awu["close"], method="log")
#
# nr_days = (awu_max_draw["trough_date"]-awu_max_draw["peak_date"]).days
# nr_days_log = (awu_max_draw_log["trough_date"]-awu_max_draw_log["peak_date"]).days
#
# line = np.linspace(awu_max_draw["peak_price"], awu_max_draw["trough_price"], nr_days)
# line = pd.Series(line)
# line.index = [i for i in daterange(awu_max_draw["peak_date"], awu_max_draw["trough_date"])]
#
# line_log = np.linspace(awu_max_draw_log["peak_price"], awu_max_draw_log["trough_price"], nr_days_log)
# line_log = pd.Series(line_log)
# line_log.index = [i for i in daterange(awu_max_draw_log["peak_date"], awu_max_draw_log["trough_date"])]
#
# stonks = {f"AWU": awu["close"],
#           f"Max drawdown ${awu_max_draw['max_drawdown']}": line,
#           f"Max drawdown: {round(100 - 100*awu_max_draw_log['trough_price']/awu_max_draw_log['peak_price'], 2)}": line_log
#           }
#
# plot_function(stonks)



#  Figure 2.13:

# awu_vol = metrics.calculate_log_max_drawdown_ratio(awu["close"])
# bmg_vol = metrics.calculate_log_max_drawdown_ratio(bmg["close"])
# cuu_vol = metrics.calculate_log_max_drawdown_ratio(cuu["close"])
#
#
# stonks = {f"AWU: {round(awu_vol, 3)}": 100*awu["close"]/awu["close"][0],
#           f"BMG: {round(bmg_vol, 3)}": 100*bmg["close"]/bmg["close"][0],
#           f"CUU: {round(cuu_vol, 3)}": 100*cuu["close"]/cuu["close"][0]}
# plot_function(stonks, y_lab="Standardized price ($'s)")



#  Figure 2.14:

# awu_vol = metrics.calculate_calmar_ratio(awu["close"], years_past=10)
# bmg_vol = metrics.calculate_calmar_ratio(bmg["close"], years_past=10)
# cuu_vol = metrics.calculate_calmar_ratio(cuu["close"], years_past=10)
#
#
# stonks = {f"AWU: {round(awu_vol, 3)}": 100*awu["close"]/awu["close"][0],
#           f"BMG: {round(bmg_vol, 3)}": 100*bmg["close"]/bmg["close"][0],
#           f"CUU: {round(cuu_vol, 3)}": 100*cuu["close"]/cuu["close"][0]}
# plot_function(stonks, y_lab="Standardized price ($'s)")



#  Figure 2.15:

# from sklearn.linear_model import LinearRegression
#
#
# t = np.arange(0, awu["close"].shape[0]).reshape(-1, 1)
#
# reg = LinearRegression().fit(t, awu["close"])
# r_sq = reg.score(t, awu["close"])
# print(r_sq)
# awu_vol = metrics.calculate_pure_profit_score(awu["close"])
#
# best_line = np.linspace(reg.intercept_, reg.coef_*t[-1]+reg.intercept_, len(awu["close"])).reshape(-1)
# best_line = pd.Series(best_line)
# best_line.index = [i for i in awu["close"].index]
#
# stonks = {f"AWU: {round(awu_vol*100, 3)}%": awu["close"],
#           "Best-fit line": best_line}
# plot_function(stonks, y_lab="Standardized price ($'s)")


#  Figure 2.16:

from sklearn.linear_model import LinearRegression


t = np.arange(0, bmg["close"].shape[0]).reshape(-1, 1)

reg = LinearRegression().fit(t, bmg["close"])
r_sq = reg.score(t, bmg["close"])
print(r_sq)
bmg_vol = metrics.calculate_pure_profit_score(bmg["close"])

best_line = np.linspace(reg.intercept_, reg.coef_*t[-1]+reg.intercept_, len(bmg["close"])).reshape(-1)
best_line = pd.Series(best_line)
best_line.index = [i for i in bmg["close"].index]

stonks = {f"BMG: {round(bmg_vol*100, 3)}%": bmg["close"],
          "Best-fit line": best_line}
plot_function(stonks, y_lab="Standardized price ($'s)")