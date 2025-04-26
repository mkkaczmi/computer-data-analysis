import os
import numpy as np

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

def second_table(data):
    results = [['Cecha', 'Minimum', 'Średnia arytmetyczna', 'Odchylenie standardowe', 'Mediana Q2', 'Mediana Q1', 'Mediana Q3', 'Maksimum']]
    
    # Convert data to numpy array for easier calculations
    data_array = np.array(data)
    
    # Characteristics and their corresponding indexes
    characteristics = {
        'Długość działki kielicha (cm)': 0,
        'Szerokość działki kielicha (cm)': 1,
        'Długość płatka (cm)': 2,
        'Szerokość płatka (cm)': 3
    }
    
    for text, column in characteristics.items():
        column_data = data_array[:, column]
        min_val = round(np.min(column_data), 2)
        avg_val = round(np.mean(column_data), 2)
        std_dev = round(np.std(column_data, ddof=1), 2)  # ddof=1 for standard deviation of sample
        median_q2 = round(np.median(column_data), 2)
        median_q1 = round(np.percentile(column_data, 25), 2)
        median_q3 = round(np.percentile(column_data, 75), 2)
        max_val = round(np.max(column_data), 2)

        results.append([text, min_val, avg_val, std_dev, median_q2, median_q1, median_q3, max_val])

    save_table("second_table.txt", results)

def tables(data):
    first_table(data)
    second_table(data)
