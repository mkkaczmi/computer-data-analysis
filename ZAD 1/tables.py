import pandas as pd

def species_count(df):
    last_column = df.columns[-1]

    counts = {
        'setosa': (df[last_column] == 0).sum(),
        'versicolor': (df[last_column] == 1).sum(),
        'virginica': (df[last_column] == 2).sum()
    }

    return counts

def get_total_count(counts):
    return sum(counts.values())

def table_species(df):
    counts = species_count(df)
    total_count = get_total_count(counts)

    data = []
    for kind, count_of_kind in counts.items():
        percentage = round(count_of_kind / total_count * 100, 2)
        data.append([kind, count_of_kind, f'{percentage}%'])

    data.append(['Razem', total_count, '100%'])
    result_df = pd.DataFrame(data, columns=['Gatunek', 'Liczebność', 'Procent'])

    print(result_df)

def tables(df):
    table_species(df)
