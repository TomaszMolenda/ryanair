from firebase_admin import db

from definition.dto import DefinitionDto


def create_item(definition_id, definition):
    return DefinitionDto(definition_id,
                         definition['destination'],
                         definition['departure_date'],
                         definition['origin'],
                         definition['arrival_date'],
                         definition['max_worth_to_pay']
                         )


def create_items(definitions):
    return_list = []
    for definition_id, definition in definitions.items():
        dto = create_item(definition_id, definition)
        return_list.append(dto)
    return return_list


class DefinitionQuery:
    __instance = None

    @staticmethod
    def get_instance():
        if DefinitionQuery.__instance is None:
            DefinitionQuery()
        return DefinitionQuery.__instance

    def __init__(self):
        if DefinitionQuery.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DefinitionQuery.__instance = self

    @staticmethod
    def list_all():
        definitions = db.reference().child('definitions').get()

        if definitions is None:
            return []

        return create_items(definitions)

    @staticmethod
    def get(definition_id):
        definition = db.reference().child('definitions').child(definition_id).get()

        assert definition

        return create_item(definition_id, definition)
