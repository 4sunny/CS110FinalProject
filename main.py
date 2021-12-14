from data_computations import Model
from data_filtering import Country
from data_visualization import Plot

csv_location = 'condensed_data.csv'

# Read data into Country objects
""" 
Feel free to try other countries by changing the Country input string! 
e.g. Country('Germany', csv_location)
The dataset we included currently supports 
[Canada, Australia, Germany, France, United States and United Kingdom] 
"""
country1 = Country('United States', csv_location)
country2 = Country('Canada', csv_location)
country3 = Country('France', csv_location)

# Model data in Model objects
model1 = Model(country1)
model2 = Model(country2)
model3 = Model(country3)

# Visualize data in Plot object
# The boxes on the left of the interactive window are interactive! Click them to toggle visibility.
# If you are using pycharm, open them in a separate window by going to
# File | Settings | Tools | Python Scientific and toggling "Show plots in tool window".
myPlot = Plot([model1, model2, model3], ['r', 'g', 'b'])

if __name__ == '__main__':
    myPlot.visualize()
