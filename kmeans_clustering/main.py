from get_data import get_data
from k_means import generate_plots

data = get_data("./data/data2.csv")
generate_plots(data)