from firebase_admin import db


class EmailRepository:
    __instance = None

    @staticmethod
    def get_instance():
        if EmailRepository.__instance is None:
            EmailRepository()
        return EmailRepository.__instance

    def __init__(self):
        if EmailRepository.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EmailRepository.__instance = self

    @staticmethod
    def save(email):
        db.reference().child('email').update(email.asdict())
        pass

    @staticmethod
    def get():
        return db.reference().child('email').get()
