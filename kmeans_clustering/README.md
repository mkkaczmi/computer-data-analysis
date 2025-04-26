# K-Means Clustering Implementation

This directory contains an implementation of the k-means clustering algorithm.

## Files

- `main.py` - Main script that runs the clustering analysis
- `k_means.py` - Core implementation of the k-means clustering algorithm
- `get_data.py` - Utility script for data retrieval
- `clusters_iterations.txt` - Results of cluster analysis
- Various scatter plot images showing different feature combinations

## Directory Structure

- `data/` - Contains input data files

## Requirements

Install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script to perform the clustering analysis:
```bash
python main.py
```

This will:
1. Load and preprocess the data
2. Perform k-means clustering
3. Generate scatter plots for different feature combinations
4. Save the results in `clusters_iterations.txt`

The implementation includes visualization of the clustering results through scatter plots of different feature combinations. 