import sys
sys.path.append("../..") # adds higher directory to python modules path
from src.pypm import metrics, data_io

df = data_io.load_eod_data('AWU')
print(metrics.calculate_cagr(df['close']))