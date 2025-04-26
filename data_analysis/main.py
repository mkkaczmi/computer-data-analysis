import numpy as np
import csv
import os
import matplotlib.pyplot as plt

########################################################
# Get data
########################################################

def get_data(file_path):
    data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append([float(value) for value in row])
    return data

########################################################
# Tables
########################################################

def save_table(filename, results, output_dir="tables/"):
    # Create folder if it's not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_dir + filename, 'w', encoding='utf-8') as file:
        # Get maximal length of string in each column for formatting
        col_widths = [max(len(str(row[i])) for row in results) for i in range(len(results[0]))]

        for row in results:
            for i, elem in enumerate(row):
                file.write(str(elem).ljust(col_widths[i] + 2))
            file.write('\n')

def species_count(data):
    setosa = 0
    versicolor = 0
    virginica = 0

    for row in data:
        if row[-1] == 0:
            setosa += 1
        elif row[-1] == 1:
            versicolor += 1
        if row[-1] == 2:
            virginica += 1
        
    counts = {
        'setosa': setosa,
        'versicolor': versicolor,
        'virginica': virginica
    }

    return counts

def first_table(data):
    counts = species_count(data)
    total_count = len(data)

    results = [['Gatunek', 'Liczebność', '%']]
    for kind, count_of_kind in counts.items():
        percentage = round(count_of_kind / total_count * 100, 1)
        results.append([kind, count_of_kind, f'{percentage}%'])

    results.append(['Razem', total_count, '100%'])

    save_table("first_table.txt", results)

def get_characteristics():
    # Characteristics and their corresponding indexes
    return {
        0: 'Długość działki kielicha',
        1: 'Szerokość działki kielicha',
        2: 'Długość płatka',
        3: 'Szerokość płatka'
    }

def second_table(data):
    results = [['Cecha', 'Minimum', 'Średnia arytmetyczna', 'Odchylenie standardowe', 'Mediana Q2', 'Mediana Q1', 'Mediana Q3', 'Maksimum']]
    
    data_array = np.array(data)
    characteristics = get_characteristics()
    
    for col_idx, text in characteristics.items():
        column_data = data_array[:, col_idx]
        min_val = round(np.min(column_data), 2)
        avg_val = round(np.mean(column_data), 2)
        std_dev = round(np.std(column_data, ddof=0), 2)
        median_q2 = round(np.median(column_data), 2)
        median_q1 = round(np.percentile(column_data, 25), 2)
        median_q3 = round(np.percentile(column_data, 75), 2)
        max_val = round(np.max(column_data), 2)

        results.append([f"{text} (cm)", min_val, avg_val, std_dev, median_q2, median_q1, median_q3, max_val])

    save_table("second_table.txt", results)

def tables(data):
    first_table(data)
    second_table(data)

########################################################
# Histograms and Boxplots
########################################################

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

    plt.hist(dataset, bins='auto', edgecolor='black')

    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel('Liczebność', fontsize=15)
    plt.title(title, fontsize=15)

    output_path = f"{output_dir}/{title.replace(' ', '_')}_hist.png"
    plt.savefig(output_path)
    plt.close()

def hist_all(data):
    characteristics = get_characteristics()
    
    # Get characteristics and their corresponding data and xlabel
    characteristics_desc = {
        name: {
            "data": get_column(data, idx),
            "xlabel": "Długość (cm)" if "Długość" in name else "Szerokość (cm)"
        }
        for idx, name in characteristics.items()
    }

    for title, description in characteristics_desc.items():
        hist(title, description)

def box(title, description, output_dir="plots/box"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    dataset = [item for item in description.values()]

    plt.boxplot(dataset)

    plt.xticks([i + 1 for i in range(len(dataset))], list(description.keys()))

    plt.title(title, fontsize=15)
    plt.xlabel('Gatunek', fontsize=15)
    plt.ylabel("Długość (cm)" if title[0] == "D" else "Szerokość (cm)", fontsize=15)

    output_path = f"{output_dir}/{title.replace(' ', '_')}_box.png"
    plt.savefig(output_path)
    plt.close()

def box_all(data):
    characteristics = get_characteristics()
    characteristics_desc = {
        name: {
            "setosa": get_column_for_species(data, idx, 0),
            "versicolor": get_column_for_species(data, idx, 1),
            "virginica": get_column_for_species(data, idx, 2),
        }
        for idx, name in characteristics.items()
    }

    for title, description in characteristics_desc.items():
        box(title, description)

def hist_box(data):
    hist_all(data)
    box_all(data)

########################################################
# Scatter Plots
########################################################

def plot(x, y, x_label, y_label, output_dir="plots/scatter"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get coefficients of the linear regression line
    a, b = np.polyfit(x, y, 1)[1], np.polyfit(x, y, 1)[0]

    plt.scatter(x, y)

    y_line = [b * xi + a for xi in x]
    plt.plot(x, y_line, color='red')

    plt.xlabel(x_label + " (cm)", fontsize=15)
    plt.ylabel(y_label + " (cm)", fontsize=15)

    # Get correlation coefficient
    r = round(np.corrcoef(x, y)[0, 1], 2) 

    title_a = f"+ {round(a, 1)}" if a >= 0 else f"- {abs(round(a, 1))}"
    plt.title(f'r = {r}; y = {round(b, 1)}x {title_a}', fontsize=15)

    output_path = f"{output_dir}/{x_label.replace(' ', '_')}_I_{y_label.replace(' ', '_')}.png"
    plt.savefig(output_path)
    plt.close()

def all_plots(data):
    pairs = []
    characteristics = get_characteristics()
    feature_indices = list(characteristics.keys())

    for i in range(len(feature_indices)):
        for j in range(i + 1, len(feature_indices)):
            pairs.append([feature_indices[i], feature_indices[j]])

    for pair in pairs:
        x, y = pair
        x_column = get_column(data, x)
        y_column = get_column(data, y)
        x_label = characteristics[x]
        y_label = characteristics[y]

        plot(x_column, y_column, x_label, y_label)
        
def scatter_plots(data):
    all_plots(data)

########################################################
# Main
########################################################

data = get_data("./data/data1.csv")

tables(data)
hist_box(data)
scatter_plots(data)