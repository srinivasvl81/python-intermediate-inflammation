"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import json

class Patient:
    def __init__(self, name: str, weight: float, height: float):
        """Patient class

        :param name: Name of patient
        :param weight: Weight in kilograms
        :param height: Height in meters
        :raises ValueError: If weight or height are not positive numbers.
        """
        if weight <= 0:
            raise ValueError("weight must be a positive number")
        if height <= 0:
            raise ValueError("height must be a positive number")
        self.name = name
        self.weight = weight
        self.height = height

    def get_body_mass_index(self):
        """Compute body mass index using weight and height attributes."""
        return compute_bmi(self.weight, self.height)

    def is_overweight(self):
        """Return True if patient BMI is above 25, False otherwise."""
        return self.get_body_mass_index() > 25

def compute_bmi(weight: float, height: float) -> float:
    """Calculate body mass index from weight and height.

    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: Body mass index (kg/m²)
    """
    return weight / height ** 2

def load_json(filename):
    """Load a numpy array from a JSON document.
    
    Expected format:
    [
      {
        "observations": [0, 1]
      },
      {
        "observations": [0, 2]
      }    
    ]
    :param filename: Filename of CSV to load
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]

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

