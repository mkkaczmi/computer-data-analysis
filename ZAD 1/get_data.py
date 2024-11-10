import pandas as pd

def get_data(file_path):
    df = pd.read_csv(file_path)

    return df