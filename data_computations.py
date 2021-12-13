import numpy as np
from classes import Country
import scipy.optimize
import sklearn
from sklearn import linear_model


def optimize_curve(x: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Return the numpy array ....

    Preconditions:
      - x != np. array([])
      - a != np. array([])
      - b != np. array([])
    """
    return np.exp2((a * x) + b)


class Model:
    country: Country
    ifr: np.ndarray
    x_train: np.ndarray
    curve: np.ndarray
    popt: np.ndarray

    def __init__(self, country: Country):
        self.country = country
        self.ifr = country.new_deaths_smoothed_per_million / country.reproduction_rate * 10

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            country.people_fully_vaccinated_per_hundred, self.ifr, test_size=0.1)
        self.x_train = x_train
        self.popt, _ = scipy.optimize.curve_fit(optimize_curve, x_train.flatten(), y_train.flatten(), p0=([0.1, 7]))
        self.curve = optimize_curve(x_train, *self.popt)


