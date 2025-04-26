import matplotlib.pyplot as plt
import numpy as np
from hist_box import get_column
import os

def characteristics(column_index):
    data = ["Długość działki kielicha", "Szerokość działki kielicha", "Długość płatka", "Szerokość płatka"]

    return data[column_index]


def plot(x, y, x_mean, y_mean, x_label, y_label, output_dir="plots/scatter"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    a, b = np.polyfit(x, y, 1)[1], np.polyfit(x, y, 1)[0]

    plt.scatter(x, y)

    y_line = [b * xi + a for xi in x]
    plt.plot(x, y_line, color='red',)

    plt.xlabel(x_label + " (cm)")
    plt.ylabel(y_label + " (cm)")

    r = round(np.corrcoef(x, y)[0, 1], 2)
    title_a = f"+ {round(a, 1)}" if a >= 0 else f"- {abs(round(a, 1))}"
    plt.title(f'r = {r}; y = {round(b, 1)}x {title_a}')

    output_path = f"{output_dir}/{x_label.replace(' ', '_')}_I_{y_label.replace(' ', '_')}.png"
    plt.savefig(output_path)
    plt.close()

def all_plots(data):
    pairs = []

    for i in range(len(data[0]) - 1):
        for j in range(i + 1, len(data[0]) - 1):
            pairs.append([i, j])

    for pair in pairs:
        x, y = pair

        x_column = get_column(data, x)
        y_column = get_column(data, y)
        x_mean = np.mean(x_column)
        y_mean = np.mean(y_column)
        x_label = characteristics(x)
        y_label = characteristics(y)

        plot(x_column, y_column, x_mean, y_mean, x_label, y_label)
        
def scatter_plots(data):
    all_plots(data)