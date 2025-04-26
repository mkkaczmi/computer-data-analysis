import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, accuracy_score
import itertools
import os

def load_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, :-1]  # Wszystkie cechy oprócz ostatniej kolumny
    y = data[:, -1]   # Ostatnia kolumna (etykiety klas)
    return X, y

def get_feature_description(feature_indices):
    if len(feature_indices) == 4:  # Jeśli używane są wszystkie cechy
        return "wszystkie cechy"
    
    feature_names = [
        "długość działki kielicha",
        "szerokość działki kielicha",
        "długość płatka",
        "szerokość płatka"
    ]
    return ", ".join(feature_names[i] for i in feature_indices)

def save_confusion_matrix(matrix, k, features, output_dir="plots"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    plt.figure(figsize=(8, 6))
    plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.Blues)
    feature_desc = get_feature_description(features)
    plt.title(f'Macierz pomyłek (k={k})\nCechy: {feature_desc}', fontsize=16)
    
    # plt.colorbar()
    classes = ['setosa', 'versicolor', 'virginica']
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    
    # Dodawanie tekstu do macierzy
    for i in range(len(classes)):
        for j in range(len(classes)):
            plt.text(j, i, str(matrix[i, j]),
                    horizontalalignment="center",
                    color="white" if matrix[i, j] > matrix.max() / 2 else "black")
    
    plt.ylabel('Rzeczywiste wartości', fontsize=15)
    plt.xlabel('Przewidywane wartości', fontsize=15)
    plt.tight_layout()
    
    feature_str = '_'.join(str(f) for f in features)
    plt.savefig(f"{output_dir}/confusion_matrix_k{k}_{feature_str}.png")
    plt.close()

def plot_accuracy(k_values, accuracies, features, output_dir="plots"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    plt.figure(figsize=(10, 6))
    k_values_list = list(k_values)
    
    plt.bar(k_values_list, accuracies, width=0.8, color='skyblue', edgecolor='black')
    feature_desc = get_feature_description(features)
    plt.title(f'Dokładność klasyfikacji dla różnych wartości k\n({feature_desc})', fontsize=16)
    plt.xlabel('Liczba sąsiadów (k)', fontsize=15)
    plt.ylabel('Dokładność (%)', fontsize=15)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.xticks(k_values_list)
    
    # Dodawanie etykiety wartości nad słupkami
    for i, v in enumerate(accuracies):
        plt.text(k_values_list[i], v + 0.5, f'{v:.1f}%', 
                horizontalalignment='center',
                fontsize=8)
    
    # Dostosowanie zakresu osi y, aby zmieścić etykiety
    plt.ylim(0, 105)
    
    feature_str = '_'.join(str(f) for f in features)
    plt.savefig(f"{output_dir}/accuracy_plot_{feature_str}.png")
    plt.close()

def run_knn_analysis(train_X, train_y, test_X, test_y, feature_indices, k_range=range(1, 16)):
    # Wybór cech
    train_data = train_X[:, feature_indices]
    test_data = test_X[:, feature_indices]
    
    # Przeskalowanie danych
    scaler = MinMaxScaler()
    train_scaled = scaler.fit_transform(train_data)
    test_scaled = scaler.transform(test_data)
    
    # Testowanie różnych wartości k
    accuracies = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k, weights='uniform')
        knn.fit(train_scaled, train_y)
        
        # Wykonanie predykcji i obliczenie dokładności
        predictions = knn.predict(test_scaled)
        accuracy = accuracy_score(test_y, predictions) * 100
        accuracies.append(accuracy)
    
    # Znalezienie najlepszego k
    best_k_idx = np.argmax(accuracies)
    best_k = k_range[best_k_idx]
    
    # Uzyskanie predykcji dla najlepszego k
    best_knn = KNeighborsClassifier(n_neighbors=best_k, weights='uniform')
    best_knn.fit(train_scaled, train_y)
    best_predictions = best_knn.predict(test_scaled)
    
    # Utworzenie i zapis macierzy pomyłek
    conf_matrix = confusion_matrix(test_y, best_predictions)
    save_confusion_matrix(conf_matrix, best_k, feature_indices)
    
    # Rysowanie wykresu dokładności
    plot_accuracy(k_range, accuracies, feature_indices)


# MAIN

# Wczytanie danych
train_X, train_y = load_data("data/data3_train.csv")
test_X, test_y = load_data("data/data3_test.csv")

# Przeprowadzenie analizy dla wszystkich cech
all_features = list(range(4))
run_knn_analysis(train_X, train_y, test_X, test_y, all_features)

# Przeprowadzenie analizy dla par cech
feature_pairs = list(itertools.combinations(range(4), 2))
for pair in feature_pairs:
    run_knn_analysis(train_X, train_y, test_X, test_y, pair)