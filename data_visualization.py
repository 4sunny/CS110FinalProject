"""CSC110 Fall 2021 Final Project: Modelling COVID-19 Infection Fatality Rate Based On Percentage Of
Population Vaccinated Using Linear Regression

This file is responsible for visualizing the model and data from the Model class in an interactive
manner.
Inspiration:
https://ourworldindata.org/explorers/coronavirus-data-explorer
"""
import matplotlib.lines
import matplotlib.figure
from matplotlib.widgets import CheckButtons
from matplotlib import pyplot
import numpy as np
from data_computations import Model


class Plot:
    """A plot visualizing the data

     Instance Attributes:
      - models: list of models
      - fig: matplotlib figure object
      - colors: list of colors as matplotlib color codes
      - plots: list of matplotlib subplots for our models
        Each model will have one for its real data, and another for its curve
      - labels: list of labels for each plot


    Representation Invariants:
        - self.models != []
    """
    models: list[Model]
    fig: matplotlib.figure.Figure
    colors: list[str]
    plots: list[matplotlib.lines.Line2D]
    labels: list[str]

    def __init__(self, models: list[Model], colors: list[str]) -> None:
        self.models = models
        self.colors = colors
        self.fig = pyplot.figure()

        plots = []
        labels = []
        ax = self.fig.subplots()
        for i in range(len(models)):
            model = models[i]
            plots.append(
                ax.plot(model.country.people_fully_vaccinated_per_hundred, model.country.get_ifr(),
                        'o', markersize=2, color=colors[i], label=model.country.location,
                        visible=True))
            plots.append(
                ax.plot(np.arange(0, 101), model.curve, color=colors[i],
                        label=f"{model.country.location} fit", visible=False))
            labels.append(model.country.location)
            labels.append(f"{model.country.location} fit")

        self.plots = plots
        self.labels = labels

    def select_plot(self, label: str) -> None:
        """Toggles the visibility of selected plot

            Preconditions:
              - label != ''
              - self.labels != []

        """
        # find index of plot
        index = self.labels.index(label)

        # set the graph to visible
        self.plots[index][0].set_visible(not self.plots[index][0].get_visible())
        self.fig.canvas.draw()

    def visualize(self) -> None:
        """Launches the interactive window with appropriate attributes


            Preconditions:
              - self.labels != []

        """
        self.fig.suptitle("%PV and IFR")
        pyplot.subplots_adjust(left=0.48, bottom=0.25)
        pyplot.xlabel("% of Population Fully Vaccinated")
        pyplot.ylabel("IFR")
        pyplot.legend()
        activated = [True, False, True, False, True, False]
        ax_check = pyplot.axes([0.02, 0.3, 0.35, 0.5])
        plot_button = CheckButtons(ax_check, self.labels, activated)

        plot_button.on_clicked(self.select_plot)
        pyplot.show()


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    import doctest

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': [],
        'extra-imports': ['matplotlib.lines', 'matplotlib.figure', 'matplotlib.widgets',
                          'matplotlib', 'numpy', 'data_computations'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })
