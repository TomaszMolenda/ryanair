class DefinitionDto(object):
    def __init__(self, id, destination, departure_date, origin, arrival_date, max_worth_to_pay):
        self.id = id
        self.destination = destination
        self.departure_date = departure_date
        self.origin = origin
        self.arrival_date = arrival_date
        self.max_worth_to_pay = max_worth_to_pay

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.destination == other.destination \
                   and self.departure_date == other.departure_date \
                   and self.origin == other.origin \
                   and self.arrival_date == other.arrival_date \
                   and self.max_worth_to_pay == other.max_worth_to_pay
        else:
            return False
