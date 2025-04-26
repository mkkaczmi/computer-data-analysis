from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def normalize(dataset):
    normalized_data = []
    for col in range(len(dataset[0])):
        col_values = [row[col] for row in dataset]
        min_val = min(col_values)
        max_val = max(col_values)
        # Przekształcanie wartości w kolumnie do zakresu [0, 1]
        normalized_col = [(value - min_val) / (max_val - min_val) for value in col_values]
        for i, norm_value in enumerate(normalized_col):
            if len(normalized_data) <= i:
                normalized_data.append([])
            normalized_data[i].append(norm_value)
    return normalized_data

def generate_plots(data):
    # Zamiana na float
    data = [[float(value) for value in row] for row in data]

    # Normalizacja danych
    normalized_data = normalize(data)

    # Klasteryzacja
    km = KMeans(n_clusters=3, random_state=42)
    km.fit(normalized_data)
    labels = km.labels_  # Etykiety przypisane do klastrów
    centroids = km.cluster_centers_  # Centroidy klastrów

    # Opisy osi
    axis_labels = [
        "długość działki kielicha [cm]",
        "szerokość działki kielicha [cm]",
        "długość płatka [cm]",
        "szerokość płatka [cm]"
    ]

    # Pary indeksów cech
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    colors = ['red', 'green', 'blue']  # Kolory dla klastrów

    # Generowanie wykresów dla każdej pary cech
    for i, (x_idx, y_idx) in enumerate(pairs):
        plt.figure()
        # Rysowanie punktów dla każdego z klastrów
        for label in set(labels):
            cluster_points = [
                (data[j][x_idx], data[j][y_idx])
                for j in range(len(labels))
                if labels[j] == label
            ]
            plt.scatter(
                [point[0] for point in cluster_points],
                [point[1] for point in cluster_points],
                color=colors[label]
            )

        # Rysowanie centroidów
        plt.scatter(
            [centroids[label][x_idx] * (max([row[x_idx] for row in data]) - min([row[x_idx] for row in data])) + min([row[x_idx] for row in data]) for label in range(3)],
            [centroids[label][y_idx] * (max([row[y_idx] for row in data]) - min([row[y_idx] for row in data])) + min([row[y_idx] for row in data]) for label in range(3)],
            c=colors, marker='D', s=150, edgecolor='black'
        )
        plt.xlabel(axis_labels[x_idx], fontsize=15)
        plt.ylabel(axis_labels[y_idx], fontsize=15)
        plt.savefig(f"scatter_{x_idx+1}_{y_idx+1}.png")
        plt.close()

    # Obliczanie WCSS
    wcss = []
    iterations = []
    for k in range(2, 11):
        km = KMeans(n_clusters=k, random_state=42)
        km.fit(normalized_data)
        wcss.append(km.inertia_)  # Suma kwadratów odległości punktów od centroidów
        iterations.append(km.n_iter_)  # Liczba iteracji do zbieżności

    # Wykres zależności WCSS od liczby klastrów
    plt.figure()
    plt.plot(range(2, 11), wcss, marker='o')
    plt.xlabel("Liczba klastrów (k)", fontsize=15)
    plt.ylabel("WCSS", fontsize=15)
    plt.savefig("wcss_plot.png")
    plt.close()

    with open("clusters_iterations.txt", "w", encoding="utf-8") as file:
        for k, iteration in zip(range(2, 11), iterations):
            file.write(f"Liczba klastrów: {k}, Liczba iteracji: {iteration}\n")
