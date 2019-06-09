from firebase_admin import db

from email_dto import EmailDto
from trip.dto import TripDto, FlightDto


def create_dtos(email):
    email_from = email['email_from']
    email_to = email['email_to']
    password = email['password']

    return EmailDto(email_from, email_to, password)


def create_empty_dto():
    return EmailDto('', '', '')


class EmailQuery:
    __instance = None

    @staticmethod
    def get_instance():
        if EmailQuery.__instance is None:
            EmailQuery()
        return EmailQuery.__instance

    def __init__(self):
        if EmailQuery.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EmailQuery.__instance = self

    @staticmethod
    def get():
        email = db.reference().child('email').get()

        if email is None:
            return create_empty_dto()

        return create_dtos(email)
