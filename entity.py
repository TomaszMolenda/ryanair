import datetime


def asdictc_collection(collection_in):
    return_collection = []
    for element in collection_in:
        return_collection.append(element.asdict())
    return return_collection


class Definition(object):
    def __init__(self, destination, departure_date, origin, arrival_date, adult, teen, child, flex_days, max_worth_to_pay):
        self.destination = destination
        self.departure_date = departure_date
        self.origin = origin
        self.arrival_date = arrival_date
        self.adult = adult
        self.teen = teen
        self.child = child
        self.flex_days = flex_days
        self.max_worth_to_pay = max_worth_to_pay

    def asdict(self):
            return {'destination': self.destination,
                    'departure_date': self.departure_date,
                    'origin': self.origin,
                    'arrival_date': self.arrival_date,
                    'adult': self.adult,
                    'teen': self.teen,
                    'child': self.child,
                    'flex_days': self.flex_days,
                    'max_worth_to_pay': self.max_worth_to_pay
                    }

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.destination == other.destination \
                   and self.departure_date == other.departure_date \
                   and self.origin == other.origin \
                   and self.arrival_date == other.arrival_date \
                   and self.adult == other.adult \
                   and self.teen == other.teen \
                   and self.child == other.child \
                   and self.flex_days == other.flex_days \
                   and self.max_worth_to_pay == other.max_worth_to_pay
        else:
            return False


class CheckedTrip(object):
    def __init__(self, trip_to_destination, trip_to_origin):
        self.trip_to_destination = trip_to_destination
        self.trip_to_origin = trip_to_origin
        self.date = datetime.datetime.now().isoformat()

    def asdict(self):
            return {'trip_to_destination': self.trip_to_destination.asdict(),
                    'trip_to_origin': self.trip_to_origin.asdict(),
                    'date': self.date}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.trip_to_destination == other.trip_to_destination \
                   and self.trip_to_origin == other.trip_to_origin \
                   and self.date == other.date
        else:
            return False


class Trip(object):
    def __init__(self, origin, destination, dates):
        self.origin = origin
        self.destination = destination
        self.dates = dates

    def asdict(self):
        return {'origin': self.origin,
                'destination': self.destination,
                'dates': asdictc_collection(self.dates)}

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

    def asdict(self):
        return {'departure_date': self.departure_date,
                'flights': asdictc_collection(self.flights)}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.departure_date == other.departure_date
        else:
            return False


class Flight(object):
    def __init__(self, flight_number, fares):
        self.flight_number = flight_number
        self.fares = fares

    def asdict(self):
        return {'flight_number': self.flight_number,
                'fares': asdictc_collection(self.fares)}

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

    def asdict(self):
        return {'type': self.type,
                'amount': self.amount,
                'currency': self.currency}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.type == other.type \
                   and self.amount == other.amount \
                   and self.currency == other.currency
        else:
            return False
