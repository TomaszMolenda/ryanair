import datetime


class CheckedTrip(object):
    def __init__(self, trip_to_destination, trip_to_origin):
        self.trip_to_destination = trip_to_destination
        self.trip_to_origin = trip_to_origin
        self.date = datetime.datetime.now()


class Trip(object):
    def __init__(self, origin, destination, dates):
        self.origin = origin
        self.destination = destination
        self.dates = dates

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.origin == other.origin \
                   and self.destination == other.destination
        else:
            return False


class Date(object):
    def __init__(self, departure_date, flights):
        self.departure_date = departure_date
        self.flights = flights

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.departure_date == other.departure_date
        else:
            return False


class Flight(object):
    def __init__(self, flight_number, fares):
        self.flight_number = flight_number
        self.fares = fares

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.flight_number == other.flight_number
        else:
            return False


class Fare(object):
    def __init__(self, type, amount, currency):
        self.type = type
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.type == other.type \
                   and self.amount == other.amount \
                   and self.currency == other.currency
        else:
            return False
