from factory import DefinitionFactory
from repository import DefinitionRepository


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
