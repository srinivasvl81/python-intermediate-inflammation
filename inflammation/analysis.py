"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np
import argparse

from inflammation import models, views
import json

class JSONDataSource():
    """ Loads the JSON data files from a given path """
    def __init__(self, path):
        self.path = path
        self.data = None
        pass

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.path, "inflammation*.json"))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.path}")
        self.data = map(models.load_json, data_file_paths)
        return self.data
    

class CSVDataSource():
    def __init__(self, path):
        self.path = path
        self.data = None
        pass

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.path, "inflammation*.csv"))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.path}")
        self.data = map(models.load_csv, data_file_paths)
        return self.data

def load_inflammation_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, "inflammation*.csv"))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
    
    data = map(models.load_csv, data_file_paths)
    return data

def compute_standard_deviation_by_day(data):
    """Computes the daily standard deviation by day for a given data"""
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    return np.std(means_by_day_matrix, axis=0)


def analyse_data(data_dir):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    # data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    # if len(data_file_paths) == 0:
    #     raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
    # data = map(models.load_csv, data_file_paths)

    data_source = CSVDataSource(data_dir)
    data = data_source.load_inflammation_data()

    # data = load_inflammation_data(data_dir)

    daily_standard_deviation = compute_standard_deviation_by_day(data)
    # print(daily_standard_deviation)

    # graph_data = {
    #     'standard deviation by day': daily_standard_deviation,
    # }
    # views.visualize(graph_data)

    return daily_standard_deviation


if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Calculate standard deviation by day between datasets."
    )
    
    # Add the data_dir argument
    parser.add_argument(
        'data_dir', 
        type=str, 
        help="Path to the directory containing the inflammation CSV files."
    )
    
    # Parse the arguments from the command line
    args = parser.parse_args()
    
    # Run the function using the provided argument
    analyse_data(args.data_dir)