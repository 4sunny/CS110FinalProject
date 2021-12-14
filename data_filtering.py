"""CSC110 Fall 2021 Final Project: Modelling COVID-19 Infection Fatality Rate Based On Percentage Of
Population Vaccinated Using Linear Regression

This file is responsible for reading data from the csv file, filtering it, and then converting it
into a python class Country.
"""
import csv
import numpy as np


class Country:
    """A country with related COVID-19 data

     Instance Attributes:
      - location: the name of the country
      - new_deaths_smoothed_per_million: the country's new deaths per million people,
      in chronological order
      - people_fully_vaccinated_per_hundred: the country's population fully vaccinated per hundred,
      in chronological order
      - reproduction_rate: the rate at which the virus (COVID-19) reproduces

    Representation Invariants:
        - self.location != ''
    """
    location: str
    new_deaths_smoothed_per_million: np.ndarray
    people_fully_vaccinated_per_hundred: np.ndarray
    reproduction_rate: np.ndarray

    def __init__(self, location: str, csv_file: str) -> None:
        self.location = location
        data = read_csv_file(csv_file, self.location)
        self.new_deaths_smoothed_per_million = np.array([row[1] for row in data], dtype=float)
        self.people_fully_vaccinated_per_hundred = np.array([row[2] for row in data], dtype=float)
        self.reproduction_rate = np.array([row[3] for row in data], dtype=float)

    def get_ifr(self) -> np.ndarray:
        """Returns Infection Fatality Rate (IFR) of country

        return value is numpy array of floats.
        """

        return self.new_deaths_smoothed_per_million / self.reproduction_rate * 10


def not_empty(header: list, row: list) -> bool:
    """Return whether all elements of row are non-empty

    Preconditions:
      - header != []
      - row != []

    """
    return '' not in [row[header.index('location')],
                      row[header.index('new_deaths_smoothed_per_million')],
                      row[header.index('people_fully_vaccinated_per_hundred')],
                      row[header.index('reproduction_rate')]]


def read_csv_file(filename: str, country: str) -> list[list[str]]:
    """Return the data stored in a csv file with the given filename.

    The return value is a list of lists with str elements

    Preconditions:
      - filename refers to a valid csv file with headers
      - country represented in csv file

    >>> data = read_csv_file('../data/owid-covid-data.csv', 'Canada')
    >>> data[0] == ['Canada', '3.055', '0.0', '1.01']
    True

    """

    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [[row[header.index('location')],
                 row[header.index('new_deaths_smoothed_per_million')],
                 row[header.index('people_fully_vaccinated_per_hundred')],
                 row[header.index('reproduction_rate')]]
                for row in reader if row[2] == country if not_empty(header, row)]

    return data


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    import doctest

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': ['open'],
        'extra-imports': ['csv', 'numpy'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })
