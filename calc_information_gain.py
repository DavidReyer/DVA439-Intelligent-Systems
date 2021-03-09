import pandas as pd
import numpy as np
import math
from scipy.stats import entropy


def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = np.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)

    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            # use log from math and set base to 2
            entropy += prob * math.log(prob, 2)

    return -entropy


def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])

    # Find the unique values in the column
    values = data[split_name].unique()

    # Make subsets of the data, based on the unique values
    splits = []
    for value in values:
        splits.append(data[data[split_name] == value])

    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in splits:
        prob = (subset.shape[0] / data.shape[0])
        to_subtract += prob * calc_entropy(subset[target_name])

    # Return information gain
    return original_entropy - to_subtract


def highest_info_gain(dataset, columns, target_col):
    # Intialize an empty dictionary for information gains
    information_gains = {}

    # Iterate through each column name in our list
    for col in columns:
        # Find the information gain for the column
        information_gain = calc_information_gain(dataset, col, target_col)
        # Add the information gain to our dictionary using the column name as the ekey
        information_gains[col] = information_gain

        # Return the key with the highest value
    return max(information_gains, key=information_gains.get), information_gains


dataset = pd.read_csv('datasets/1/xAPI-Edu-Data.csv')
columns = dataset.columns

abstraction_dict = {}
for col in columns:
    if dataset[col].dtype != np.int64:
        col_dict = {}
        for i, item in enumerate(dataset[col].unique()):
            col_dict[item] = i
        abstraction_dict[col] = col_dict

abstracted_dataset = pd.DataFrame(dataset)
for col in abstraction_dict:
    for abstraction in abstraction_dict[col]:
        abstracted_dataset[col] = abstracted_dataset[col].str.replace(abstraction, str(abstraction_dict[col][abstraction]))
    abstracted_dataset[col] = abstracted_dataset[col].astype(int)

columns = list(columns)
columns.remove('Topic')
highest_gain, all_gains = highest_info_gain(abstracted_dataset, columns, 'Topic')
print("Highest Gain: " + highest_gain + "\n")

ordered_gains = {k: v for k, v in sorted(all_gains.items(), key=lambda item: item[1], reverse=True)}
print("All Gains: ")
for key, item in ordered_gains.items():
    print(key + ": " + str(item))


entropies = {}
for col in columns:
    entropies[col] = calc_entropy(abstracted_dataset[col])
entropies = {k: v for k, v in sorted(entropies.items(), key=lambda item: item[1], reverse=True)}
print("\nEntropy")
for key, item in entropies.items():
    print(key + ": " + str(item))
