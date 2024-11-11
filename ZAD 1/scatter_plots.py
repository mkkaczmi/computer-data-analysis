from tables import mean
from hist_box import get_column
from tables import mean
import math

def correlation(x, y, x_mean, y_mean):
    numerator = 0
    denominator_x = 0
    denominator_y = 0

    for i in range(len(x)):
        x_part = x[i] - x_mean
        y_part = y[i] - y_mean
        numerator += x_part * y_part
        denominator_x += pow(x_part, 2)
        denominator_y += pow(y_part, 2)

    return numerator / math.sqrt(denominator_x * denominator_y)

def linear_regression(x, y, x_mean, y_mean):
    numerator = 0
    denominator = 0

    for i in range(len(x)):
        x_part = x[i] - x_mean
        y_part = y[i] - y_mean
        numerator += x_part * y_part
        denominator += pow(x_part, 2)
    
    b = numerator / denominator
    a = y_mean - b * x_mean

    return a, b

def pairs(data):
    print(correlation(get_column(data, 0), get_column(data, 1), mean(data, 0), mean(data, 1)))
    linear_regression(get_column(data, 0), get_column(data, 1), mean(data, 0), mean(data, 1))

def scatter_plots(data):
    pairs(data)
    return True