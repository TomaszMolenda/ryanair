class Trip(object):
    def __init__(self, flight_to_destination, flight_from_origin):
        self.flight_to_destination = flight_to_destination
        self.flight_from_origin = flight_from_origin

    def print(self):
        return '{}\n\nWylot: {}\n\nPowrót: {}\n\n'\
            .format(self.flight_to_destination, self.flight_to_destination,
                    self.flight_from_origin, self.flight_from_origin,
                    )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.flight_to_destination == other.flight_to_destination \
                   and self.flight_from_origin == other.flight_from_origin
        else:
            return False
