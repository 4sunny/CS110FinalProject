"""This is where we import the files, aggregate the data, take the columns we want, and then turn them into classes Country"""

import pandas as pd
import numpy as np
import sklearn
from matplotlib import pyplot
from matplotlib import style
import sklearn
from sklearn import linear_model
import scipy.optimize

pd.options.mode.chained_assignment = None
data = pd.read_csv('../data/owid-covid-data.csv')

column_specific_data = data[['location', 'date', 'new_cases_smoothed_per_million', 'new_deaths_smoothed_per_million',
                             'people_fully_vaccinated_per_hundred', 'reproduction_rate', "people_vaccinated_per_hundred"]]


def get_country_data(country: str):
    return column_specific_data.loc[column_specific_data['location'] == country]

country = "Japan"
data = get_country_data(country)
data['CFR'] = ((data['new_deaths_smoothed_per_million'] / data['reproduction_rate'] * 10 ))
data = data[data['people_fully_vaccinated_per_hundred'].notna()]
data = data[data['CFR'].notna()]

coco = data[['people_fully_vaccinated_per_hundred']]
loco = data[['CFR']]

style.use('fivethirtyeight')
x = np.array(coco, dtype=float)
y = np.array(loco, dtype=float)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

def func(x, a, b):
    return np.exp2((a * x) + b)

popt, _ = scipy.optimize.curve_fit(func,  x_train.flatten(),  y_train.flatten(),  p0=([0.1, 7]))


# model = linear_model.LinearRegression()
# model.fit(x_train, y_train)
# y_model = model.predict(x_train)

pyplot.scatter(data['people_fully_vaccinated_per_hundred'], data['CFR'], color="g")
pyplot.scatter(x_train, func(x_train, *popt), color='r')
pyplot.xlabel('% Of Population Vaccinated')
pyplot.ylabel('IFR')
pyplot.title(country)
pyplot.show()