from firebase_admin import db


class TripRepository:
    __instance = None

    @staticmethod
    def get_instance():
        if TripRepository.__instance is None:
            TripRepository()
        return TripRepository.__instance

    def __init__(self):
        if TripRepository.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TripRepository.__instance = self

    @staticmethod
    def delete_by_definition_id(definition_id):
        db.reference().child('trips').child(definition_id).delete()
        pass
