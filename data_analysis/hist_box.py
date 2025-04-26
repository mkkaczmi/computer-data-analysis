import matplotlib.pyplot as plt
import numpy as np
import os

def get_column(data, col_index):
    return np.array(data)[:, col_index]

def get_column_for_species(data, col_index, species_id):
    data_array = np.array(data)
    return data_array[data_array[:, -1] == species_id][:, col_index]

def hist(title, description, output_dir="plots/hist"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    xlabel = description["xlabel"]
    dataset = description["data"]

    plt.hist(dataset, edgecolor='black')

    plt.xlabel(xlabel)
    plt.ylabel('Liczebność')
    plt.title(title)

    output_path = f"{output_dir}/{title.replace(' ', '_')}_hist.png"
    plt.savefig(output_path)
    plt.close()

def hist_all(data):
    characteristics = {
        'Długość działki kielicha': {
            "data": get_column(data, 0),
            "xlabel": "Długość (cm)"
        },
        'Szerokość działki kielicha': {
            "data": get_column(data, 1),
            "xlabel": "Szerokość (cm)"
        },
        'Długość płatka': {
            "data": get_column(data, 2),
            "xlabel": "Długość (cm)"
        },
        'Szerokość płatka': {
            "data": get_column(data, 3),
            "xlabel": "Szerokość (cm)"
        }
    }

    for title, description in characteristics.items():
        hist(title, description)

def box(title, description, output_dir="plots/box"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    dataset = [item for item in description.values()]

    plt.boxplot(dataset)

    plt.xticks([i + 1 for i in range(len(dataset))], list(description.keys()))

    plt.title(title)
    plt.xlabel('Gatunek')
    plt.ylabel("Długość (cm)" if title[0] == "D" else "Szerokość (cm)")

    output_path = f"{output_dir}/{title.replace(' ', '_')}_box.png"
    plt.savefig(output_path)
    plt.close()

def box_all(data):
    characteristics = {
        'Długość działki kielicha': {
            "setosa": get_column_for_species(data, 0, 0),
            "versicolor": get_column_for_species(data, 0, 1),
            "virginica": get_column_for_species(data, 0, 2),
        },
        'Szerokość działki kielicha': {
            "setosa": get_column_for_species(data, 1, 0),
            "versicolor": get_column_for_species(data, 1, 1),
            "virginica": get_column_for_species(data, 1, 2),
        },
        'Długość płatka': {
            "setosa": get_column_for_species(data, 2, 0),
            "versicolor": get_column_for_species(data, 2, 1),
            "virginica": get_column_for_species(data, 2, 2),
        },
        'Szerokość płatka': {
            "setosa": get_column_for_species(data, 3, 0),
            "versicolor": get_column_for_species(data, 3, 1),
            "virginica": get_column_for_species(data, 3, 2),
        },
    }

    for title, description in characteristics.items():
        box(title, description)

def hist_box(data):
    hist_all(data)
    box_all(data)