# K-Nearest Neighbors Classification

This directory contains an implementation of the k-nearest neighbors (KNN) classification algorithm for the Iris dataset.

## Files

- `main.py` - Main script that implements the KNN classification and visualization
- `requirements.txt` - Required Python packages

## Directory Structure

- `data/` - Contains training and test datasets
- `plots/` - Output directory for generated visualizations

## Features

The implementation includes:
- KNN classification with different values of k
- Feature selection and analysis
- Confusion matrix visualization
- Accuracy plots for different feature combinations
- Data normalization using MinMaxScaler

## Requirements

Install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script to perform the KNN analysis:
```bash
python main.py
```

This will:
1. Load and preprocess the Iris dataset
2. Perform KNN classification with different k values
3. Generate confusion matrices and accuracy plots
4. Save all visualizations in the `plots/` directory

The analysis is performed for:
- All features combined
- All possible pairs of features 