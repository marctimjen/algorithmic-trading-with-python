### pypm/simulate_portfolio.py
import sys
sys.path.append("../..") # adds higher directory to python modules path
from src.pypm import signals, data_io, simulation, metrics
from typing import Tuple, List, Dict, Callable, NewType, Any
import pandas as pd
import matplotlib.pyplot as plt

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


def simulate_portfolio(boil_n: int = 20, sha_n: int = 20, max_pos: int = 5):

    bollinger_n = boil_n
    sharpe_n = sha_n

    # Load in data
    symbols: List[str] = data_io.get_all_symbols()
    prices: pd.DataFrame = data_io.load_eod_matrix(symbols)

    # Use the bollinger band outer band crossorver as a signal
    _bollinger = signals.create_bollinger_band_signal
    signal = prices.apply(_bollinger, args=(bollinger_n,), axis=0)

    # Use a rolling sharpe ratio approximation as a preference matrix
    _sharpe = metrics.calculate_rolling_sharpe_ratio
    preference = prices.apply(_sharpe, args=(sharpe_n, ), axis=0)

    # Run the simulator
    simulator = simulation.SimpleSimulator(
        initial_cash=10000,
        max_active_positions=max_pos,
        percent_slippage=0.0005,
        trade_fee=1,
    )
    simulator.simulate(prices, signal, preference)

    # Print results
    # simulator.portfolio_history.print_position_summaries()
    # simulator.print_initial_parameters()
    # simulator.portfolio_history.print_summary()
    # simulator.portfolio_history.plot()
    return simulator

if __name__ == '__main__':
    pass
    # ja = []
    # ls = []
    # for i in range(5, 500 + 1, 5):
    #     sim = simulate_portfolio(boil_n = i)
    #     ls.append(sim.portfolio_history.excess_cagr*100)
    #     ja.append(sim.portfolio_history.jensens_alpha)
    # print(ls)
    # # figure 4.5
    # plt.plot(ls)
    # plt.show()
    #
    # # figure 4.6
    # plt.plot(ja)
    # plt.show()


    # sha = []
    # for i in range(5, 500 + 1, 5):
    #     sim = simulate_portfolio(sha_n = i)
    #     sha.append(sim.portfolio_history.sharpe_ratio)
    #
    # # figure 4.7
    # plt.plot(sha)
    # plt.show()

    # pos = []
    # sha = []
    # for i in range(1, 100, 2):
    #     sim = simulate_portfolio(max_pos = i)
    #     pos.append(sim.portfolio_history.excess_cagr*100)
    #     sha.append(sim.portfolio_history.sharpe_ratio)
    #
    # # figure 4.8
    # plt.plot(pos)
    # plt.show()
    #
    # # figure 4.9
    # plt.plot(sha)
    # plt.show()


    # eq = sim.portfolio_history.equity_series
    # spy = data_io.load_spy_data()
    # stonks = {"Equity curve": eq,
    #           "S&P 500 Portfolio": spy["close"].div(spy["close"].iloc[0]).mul(10000)}
    # plot_function(stonks)
    
# Returns ...
# Initial Cash: $10000 
# Maximum Number of Assets: 5
#
# Equity: $39758.61
# Percent Return: 297.59%
# S&P 500 Return: 184.00%
#
# Number of trades: 1835
# Average active trades: 4.83
#
# CAGR: 14.82%
# S&P 500 CAGR: 11.02%
# Excess CAGR: 3.80%
#
# Annualized Volatility: 17.93%
# Sharpe Ratio: 0.83
# Jensen's Alpha: 0.000147
#
# Dollar Max Drawdown: $10594.83
# Percent Max Drawdown: 30.03%
# Log Max Drawdown Ratio: 1.02