from data_filtering import read_csv_file
import numpy as np


class Country:
    """A country with related COVID-19 data

     Instance Attributes:
      - location: the name of the country
      - new_deaths_smoothed_per_million: the country's new deaths per million people, in chronological order
      - people_fully_vaccinated_per_hundred: the country's population fully vaccinated per hundred, in chronological order
      - reproduction_rate: the rate at which the virus (COVID-19) reproduces

    Representation Invariants:
        - self.location != ''
        - ...
        - ...
    """
    location: str
    new_deaths_smoothed_per_million: np.ndarray
    people_fully_vaccinated_per_hundred: np.ndarray
    reproduction_rate: np.ndarray

    def __init__(self, location, csv):
        self.location = location
        data = read_csv_file(csv, self.location)
        self.new_deaths_smoothed_per_million = np.array([row[1] for row in data], dtype=float)
        self.people_fully_vaccinated_per_hundred = np.array([row[2] for row in data], dtype=float)
        self.reproduction_rate = np.array([row[3] for row in data], dtype=float)
