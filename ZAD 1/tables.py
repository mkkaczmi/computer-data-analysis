import pandas as pd

def species_count(data):
    setosa = 0
    versicolor = 0
    virginica = 0

    for row in data:
        if row[4] == 0:
            setosa += 1
        elif row[4] == 1:
            versicolor += 1
        if row[4] == 2:
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

    results = [["Gatunek", "Liczebność", "%"]]
    for kind, count_of_kind in counts.items():
        percentage = round(count_of_kind / total_count * 100, 1)
        results.append([kind, count_of_kind, f'{percentage}%'])

    results.append(['Razem', total_count, '100%'])

    # Get maximal length of string in table
    col_widths = [max(len(str(row[i])) for row in results) for i in range(len(results[0]))]

    for row in results:
        for i, elem in enumerate(row):
            print(str(elem).ljust(col_widths[i] + 2), end='')
        print()

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

def second_table(df):
    print(find_min(df, 0), find_max(df, 0))
    return True


def tables(data):
    first_table(data)
    second_table(data)
