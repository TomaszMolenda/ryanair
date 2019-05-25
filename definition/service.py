from definition.factory import DefinitionFactory
from definition.repository import DefinitionRepository
from trip.repository import TripRepository


class ApplicationService:
    __instance = None

    @staticmethod
    def get_instance():
        if ApplicationService.__instance is None:
            ApplicationService()
        return ApplicationService.__instance

    def __init__(self):
        if ApplicationService.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ApplicationService.__instance = self

    @staticmethod
    def save_definition(request):
        definition_factory = DefinitionFactory.get_instance()
        definition_repository = DefinitionRepository.get_instance()

        definition = definition_factory.create_definition(request)
        definition_repository.save(definition)
        pass

    @staticmethod
    def delete_definition(definition_id):
        definition_repository = DefinitionRepository.get_instance()
        trip_repository = TripRepository.get_instance()

        definition_repository.delete(definition_id)
        trip_repository.delete_by_definition_id(definition_id)
        pass
