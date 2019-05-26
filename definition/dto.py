class DefinitionDto(object):
    def __init__(self, id, destination, departure_date, origin, arrival_date, adult, teen, child, flex_days, max_worth_to_pay):
        self.id = id
        self.destination = destination
        self.departure_date = departure_date
        self.origin = origin
        self.arrival_date = arrival_date
        self.adult = adult
        self.teen = teen
        self.child = child
        self.flex_days = flex_days
        self.max_worth_to_pay = max_worth_to_pay

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id \
                   and self.destination == other.destination \
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
