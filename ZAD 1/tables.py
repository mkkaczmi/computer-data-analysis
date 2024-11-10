import math
import os

def save_table(filename, results, output_dir="tables/"):
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

    save_table("first_table", results)

def find_min(data, col_index):
    min_value = data[0][col_index]

    for i in range(len(data)):
        if data[i][col_index] < min_value:
            min_value = data[i][col_index]

    return round(min_value, 2)

def find_max(data, col_index):
    max_value = data[0][col_index]

    for i in range(len(data)):
        if data[i][col_index] > max_value:
            max_value = data[i][col_index]

    return round(max_value, 2)

def mean(data, col_index):
    sum_value = 0

    for i in range(len(data)):
        sum_value += data[i][col_index]

    return round(sum_value / len(data), 2)

def standard_deviation(data, mean, col_index):
    numerator = 0

    for i in range(len(data)):
        numerator += pow(data[i][col_index] - mean, 2)
    
    return round(math.sqrt(numerator / len(data)), 2)

def median(column):
    median = 0
    index_1 = None
    index_2 = None

    if len(column) % 2 == 0:
        index_1 = int(len(column) / 2)
        median = column[index_1]
    else:
        index_1 = int(len(column) / 2)
        index_2 = int(len(column) / 2) + 1
        median = (column[index_1] + column[index_2]) / 2
    
    return median, index_1, index_2

def median_for_qs(data, col_index):
    column = []

    for i in range(len(data)):
        column.append(data[i][col_index])

    column = sorted(column)
    
    median_q2 = median(column)
    median_q1 = median(column[:median_q2[1] - 1])

    # Check if median was calculated for odd dataset
    if median_q2[2] != None:
        median_q3 = median(column[median_q2[2] + 1:])
    else:
        median_q3 = median(column[median_q2[1] + 1:])

    return[round(median_q2[0], 2), round(median_q1[0], 2), round(median_q3[0], 2)]

def second_table(data):
    results = [['Cecha', 'Minimum', 'Średnia arytmetyczna', 'Odchylenie standardowe', 'Mediana Q2', 'Mediana Q1', 'Mediana Q3', 'Maksimum']]
    
    # Characteristics and their corresponding indexes
    characteristics = {
        'Długość działki kielicha (cm)': 0,
        'Szerokość działki kielicha (cm)': 1,
        'Długość płatka (cm)': 2,
        'Szerokość płatka (cm)': 3
    }
    
    for text, column in characteristics.items():
        min_val = find_min(data, column)
        avg_val = mean(data, column)
        std_dev = standard_deviation(data, avg_val, column)
        median_q2 = median_for_qs(data, column)[0]
        median_q1 = median_for_qs(data, column)[1]
        median_q3 = median_for_qs(data, column)[2]
        max_val = find_max(data, column)

        results.append([text, min_val, avg_val, std_dev, median_q2, median_q1, median_q3, max_val])

    save_table("second_table", results)

def tables(data):
    first_table(data)
    second_table(data)
