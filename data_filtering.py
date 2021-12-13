import csv


def not_empty(header: list, row: list) -> bool:
    """Return whether all elements of row are non-empty

    Preconditions:
      - header != []
      - row != []

    """
    return '' not in [row[header.index('location')], row[header.index('new_deaths_smoothed_per_million')],
                      row[header.index(
                          'people_fully_vaccinated_per_hundred')], row[header.index('reproduction_rate')]]


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
        data = [[row[header.index('location')], row[header.index('new_deaths_smoothed_per_million')], row[header.index(
            'people_fully_vaccinated_per_hundred')], row[header.index('reproduction_rate')]]
                for row in reader if row[2] == country if not_empty(header, row)]

    return data
