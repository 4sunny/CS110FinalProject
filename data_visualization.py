""" Data Visualizing"""

from matplotlib import pyplot
from matplotlib import style
from data_computations import Model
from classes import Country


def visualize(model: Model):
    pyplot.scatter(model.country.people_fully_vaccinated_per_hundred, model.ifr, color="g")
    pyplot.scatter(model.x_train, model.curve, color='r')
    pyplot.xlabel('% Of Population Vaccinated')
    pyplot.ylabel('IFR')
    pyplot.title(model.country.location)
    pyplot.show()
