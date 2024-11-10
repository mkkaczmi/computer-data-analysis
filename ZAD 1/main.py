from get_data import get_data
from tables import tables
from hist_box import hist_box

data = get_data("./data/data1.csv")

tables(data)
hist_box(data)