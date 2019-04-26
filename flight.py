class Flight(object):
    def __init__(self, currency, origin_name, destination_name, child_amount, teen_amount, adult_amount, ):
        self.currency = currency
        self.origin_name = origin_name
        self.destination_name = destination_name
        self.child_amount = child_amount
        self.teen_amount = teen_amount
        self.adult_amount = adult_amount

    def print(self):
        return '{}\n\nSkąd: {}\n\nDokąd: {}\n\nCena dziecko: {} {}\n\nCena młodzież: {} {}\n\n Cena dorosły: {} {}'\
            .format(self.origin_name, self.destination_name,
                    self.child_amount, self.currency,
                    self.teen_amount, self.currency,
                    self.adult_amount, self.currency)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.currency == other.currency \
                   and self.origin_name == other.origin_name \
                   and self.destination_name == other.destination_name \
                   and self.child_amount == other.child_amount \
                   and self.teen_amount == other.teen_amount \
                   and self.adult_amount == other.adult_amount
        else:
            return False
