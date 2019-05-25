from entity import Definition


class DefinitionFactory:
    __instance = None

    @staticmethod
    def get_instance():
        if DefinitionFactory.__instance is None:
            DefinitionFactory()
        return DefinitionFactory.__instance

    def __init__(self):
        if DefinitionFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DefinitionFactory.__instance = self

    @staticmethod
    def create_definition(request):
        destination = request.form['destination']
        departure_date = request.form['departure_date']
        origin = request.form['origin']
        arrival_date = request.form['arrival_date']
        adult = request.form['adult']
        teen = request.form['teen']
        child = request.form['child']
        flex_days = request.form['flex_days']
        max_worth_to_pay = request.form['max_worth_to_pay']

        return Definition(destination, departure_date, origin, arrival_date, adult, teen, child, flex_days, max_worth_to_pay)
