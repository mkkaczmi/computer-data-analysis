from get_data import get_data
from tables import tables
import pandas as pd

df = get_data("./data/data1.csv")

tables(df)