"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data:np.array)->np.array:
    """Calculate the daily mean of a 2d inflammation data array.

    :param data: a 2D data array with inflammation data (each row contains measurements)
    :return: mean of data for axis=0
    """    
    return np.mean(data, axis=0)


def daily_max(data:np.array)->np.array:
    """Calculate the daily max of a 2d inflammation data array.

    :param data: numpy array
    :return: maximum value of array
    """    
    return np.max(data, axis=0)


def daily_min(data:np.array)->np.array:
    """Calculate the daily min of a 2d inflammation data array.

    :param data: numpy array
    :return: minimum value of array
    """    
    return np.min(data, axis=0)

