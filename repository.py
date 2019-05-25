from firebase_admin import db


class DefinitionRepository:
    __instance = None

    @staticmethod
    def get_instance():
        if DefinitionRepository.__instance is None:
            DefinitionRepository()
        return DefinitionRepository.__instance

    def __init__(self):
        if DefinitionRepository.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DefinitionRepository.__instance = self

    @staticmethod
    def save(definition):
        db.reference().child('definitions').push(definition.asdict())
        pass

    @staticmethod
    def delete(definition_id):
        db.reference().child('definitions').child(definition_id).delete()
        pass
