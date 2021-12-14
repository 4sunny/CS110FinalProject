"""CSC110 Fall 2021 Final Project: Modelling COVID-19 Infection Fatality Rate Based On Percentage Of
Population Vaccinated Using Linear Regression

This file is responsible for computing the data from the Country object and forming the regression
model.
"""
import numpy as np
import scipy.optimize
import sklearn.model_selection
from data_filtering import Country


def optimize_curve(x: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """the base mathematical function used to model the relationship between ifr and %PV.

        returns a numpy array containing the outputs of the function.
    Preconditions:
      - x != np. array([])
      - a != np. array([])
      - b != np. array([])
    """
    return np.exp2((a * x) + b)


class Model:
    """A Regression Model of a country's ifr based on the its percentage of population vaccinated

         Instance Attributes:
          - country: a country object of the corresponding country
          - coefficients: the a and b values for the model
          - curve: the outputs of the function

        Representation Invariants:
            - self.coefficients != []
            - len(curve) == 100
        """
    country: Country
    coefficients: np.ndarray
    curve: np.ndarray

    def __init__(self, country: Country) -> None:
        self.country = country
        x, _, y, _ = sklearn.model_selection.train_test_split(
            country.people_fully_vaccinated_per_hundred, country.get_ifr(), test_size=0.1)

        # Getting coefficients for our curve
        self.coefficients, _ = scipy.optimize.curve_fit(optimize_curve,
                                                        x.flatten(), y.flatten(), p0=([0.1, 7]))

        # Computing our curve with the given coefficients for percentages 1-100
        self.curve = optimize_curve(np.arange(0, 101), *self.coefficients)

    def get_predicted_ifr(self, percentage_vaccinated: int) -> float:
        """Returns the predicted ifr of a country given a percentage of population vaccinated.

        returns a floating point value of the predicted ifr.
       Preconditions:
          - 0 <= percentage_vaccinated <= 100
        """

        return self.curve[percentage_vaccinated - 1]


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    import doctest

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': [],
        'extra-imports': ['data_filtering', 'numpy', 'scipy.optimize', 'sklearn.model_selection'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })
