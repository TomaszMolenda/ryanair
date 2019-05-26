class TripDto(object):
    def __init__(self, checked_time, flights_to_destination, flights_to_origin):
        self.checked_time = checked_time
        self.flights_to_destination = flights_to_destination
        self.flights_to_origin = flights_to_origin

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.checked_time == other.checked_time \
                   and self.flights_to_destination == other.flights_to_destination \
                   and self.flights_to_origin == other.flights_to_origin
        else:
            return False


class FlightDto(object):
    def __init__(self, date, flight_number, adult_amount, teen_amount, child_amount):
        self.date = date
        self.flight_number = flight_number
        self.adult_amount = adult_amount
        self.teen_amount = teen_amount
        self.child_amount = child_amount

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.date == other.date \
                   and self.flight_number == other.flight_number \
                   and self.adult_amount == other.adult_amount \
                   and self.teen_amount == other.teen_amount \
                   and self.child_amount == other.child_amount
        else:
            return False

