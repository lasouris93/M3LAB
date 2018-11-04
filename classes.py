class Movie:
    def __init__(self, title, priceCode):
        self.childrens = 2
        self.regular = 0
        self.newRelease = 1
        self._title = title
        self._priceCode = priceCode

    def getPriceCode(self):
        return self.priceCode

    def getTitle(self):
        return self._title

class Rental:
    def __init__(self, movie, daysRented):
        self._movie = movie
        self._daysRented = daysRented

    def getDaysRented(self):
        return self._daysRented

    def getMovie(self):
        return self._movie

class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def addRental(self, rentals):
        self._rentals.append(rentals)

    def getName(self):
        return self._name
