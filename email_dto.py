class EmailDto(object):
    def __init__(self, email_from, email_to, password):
        self.id = id
        self.email_from = email_from
        self.email_to = email_to
        self.password = password

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id \
                   and self.email_from == other.email_from \
                   and self.email_to == other.email_to \
                   and self.password == other.password
        else:
            return False
