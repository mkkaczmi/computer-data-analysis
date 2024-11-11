import matplotlib.pyplot as plt
from tables import mean
from hist_box import get_column
from tables import mean
import math

def characteristics(column_index):
    data = ["Długość działki kielicha", "Szerokość działki kielicha", "Długość płatka", "Szerokość płatka"]

    return data[column_index]

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

def plot(x, y, x_mean, y_mean, x_label, y_label):
    a, b = linear_regression(x, y, x_mean, y_mean)

    plt.scatter(x, y, color='blue')

    y_line = [b * xi + a for xi in x]
    plt.plot(x, y_line, color='red',)

    plt.xlabel(x_label + " (cm)")
    plt.ylabel(y_label + " (cm)")

    r = round(correlation(x, y, x_mean, y_mean), 2)
    plt.title(f'r = {r}; y = {round(b, 1)}x + {round(a, 1)}')

    plt.show()

def all_plots(data):
    pairs = []

    for i in range(len(data[0]) - 1):
        for j in range(i + 1, len(data[0]) - 1):
            pairs.append([i, j])

    for pair in pairs:
        x, y = pair

        x_column = get_column(data, x)
        y_column = get_column(data, y)
        x_mean = mean(data, x)
        y_mean = mean(data, y)
        x_label = characteristics(x)
        y_label = characteristics(y)

        plot(x_column, y_column, x_mean, y_mean, x_label, y_label)
        

def scatter_plots(data):
    all_plots(data)

    return True