import matplotlib.pyplot as plt
from tables import find_min, find_max

def get_column(data, col_index):
    column = []

    for i in range(len(data)):
        column.append(data[i][col_index])

    return column

def get_bins(start, end):
    result = []

    start_calc = int(start)
    if end % 10 > 5:
        end_calc = int(end) + 1
    else:
        end_calc = int(end) + 0.5
    
    current = float(start_calc)

    while current <= end_calc:
        result.append(current)
        current += 0.5

    return result

def hist(data, title, description):
    col_index = description["index"]
    bins_list = description["bins"]
    xlabel = description["xlabel"]

    dataset = get_column(data, col_index)

    plt.hist(dataset, bins=bins_list, edgecolor='black')

    plt.xlabel(xlabel)
    plt.ylabel('Liczebność')
    plt.title(title)

    plt.show()

def hist_all(data):
    characteristics = {
        'Długość działki kielicha': {
            "index": 0,
            "xlabel": "Długość (cm)",
            "bins": get_bins(find_min(data, 0), find_max(data, 0))
        },
        'Szerokość działki kielicha': {
            "index": 1,
            "xlabel": "Szerokość (cm)",
            "bins": get_bins(find_min(data, 1), find_max(data, 1))
        },
        'Długość płatka': {
            "index": 2,
            "xlabel": "Długość (cm)",
            "bins": get_bins(find_min(data, 2), find_max(data, 2))
        },
        'Szerokość płatka': {
            "index": 3,
            "xlabel": "Szerokość (cm)",
            "bins": get_bins(find_min(data, 3), find_max(data, 3))
        }
    }

    for title, description in characteristics.items():
        hist(data, title, description)


def hist_box(data):
    hist_all(data)