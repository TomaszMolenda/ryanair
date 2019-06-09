import datetime


def asdictc_collection(collection_in):
    return_collection = []
    for element in collection_in:
        return_collection.append(element.asdict())
    return return_collection


class Definition(object):
    def __init__(self, destination, departure_date, origin, arrival_date, adult, teen, child, flex_days,
                 max_worth_to_pay):
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


def obtain_flights_to_destination(persisted_trips):
    return_list = []

    for persisted_trip in persisted_trips:
        return_list.extend(persisted_trip.flights_to_destination)

    return return_list


def obtain_flights_to_origin(persisted_trips):
    return_list = []

    for persisted_trip in persisted_trips:
        return_list.extend(persisted_trip.flights_to_origin)

    return return_list


def exist(flight, persisted_flights):
    for persisted_flight in persisted_flights:
        if flight.date == persisted_flight.date \
                and flight.flight_number == persisted_flight.flight_number \
                and flight.adult_amount == persisted_flight.adult_amount \
                and flight.teen_amount == persisted_flight.teen_amount \
                and flight.child_amount == persisted_flight.child_amount:
            return True
    return False


class CheckedTrip(object):
    def __init__(self, flights_to_destination, flights_to_origin):
        self.flights_to_destination = flights_to_destination
        self.flights_to_origin = flights_to_origin
        self.date = datetime.datetime.now().isoformat()

    def asdict(self):
        return {'flights_to_destination': asdictc_collection(self.flights_to_destination),
                'flights_to_origin': asdictc_collection(self.flights_to_origin),
                'date': self.date}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.flights_to_destination == other.flights_to_destination \
                   and self.flights_to_destination == other.flights_to_destination \
                   and self.date == other.date
        else:
            return False

    def remove_existing(self, persisted_trips):

        persisted_flights_to_destination = obtain_flights_to_destination(persisted_trips)
        persisted_flights_to_origin = obtain_flights_to_origin(persisted_trips)

        flights_to_destination_to_remove = []
        for flight_to_destination in self.flights_to_destination:
            if exist(flight_to_destination, persisted_flights_to_destination):
                flights_to_destination_to_remove.append(flight_to_destination)

        for flight_to_destination in flights_to_destination_to_remove:
            self.flights_to_destination.remove(flight_to_destination)

        flights_to_origin_to_remove = []
        for flight_to_origin in self.flights_to_origin:
            if exist(flight_to_origin, persisted_flights_to_origin):
                flights_to_origin_to_remove.append(flight_to_origin)

        for flight_to_origin in flights_to_origin_to_remove:
            self.flights_to_origin.remove(flight_to_origin)

        pass


class Flight(object):
    def __init__(self, date, flight_number, adult_amount, teen_amount, child_amount):
        self.date = date
        self.flight_number = flight_number
        self.adult_amount = adult_amount
        self.teen_amount = teen_amount
        self.child_amount = child_amount

    def asdict(self):
        return {
            'date': self.date,
            'flight_number': self.flight_number,
            'adult_amount': self.adult_amount,
            'teen_amount': self.teen_amount,
            'child_amount': self.child_amount
        }

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.flight_number == other.flight_number
        else:
            return False


class Email(object):
    def __init__(self, email_from, email_to, password, server_smtp):
        self.id = id
        self.email_from = email_from
        self.email_to = email_to
        self.password = password
        self.server_smtp = server_smtp

    def asdict(self):
        return {
            'email_from': self.email_from,
            'email_to': self.email_to,
            'password': self.password,
            'server_smtp': self.server_smtp,
        }

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id \
                   and self.email_from == other.email_from \
                   and self.email_to == other.email_to \
                   and self.password == other.password \
                   and self.server_smtp == other.server_smtp
        else:
            return False
