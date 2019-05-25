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
        destination = request.form['destination'].strip()
        departure_date = request.form['departure_date'].strip()
        origin = request.form['origin'].strip()
        arrival_date = request.form['arrival_date'].strip()
        adult = int(request.form['adult'].strip())
        teen = int(request.form['teen'].strip())
        child = int(request.form['child'].strip())
        flex_days = int(request.form['flex_days'].strip())
        max_worth_to_pay = int(request.form['max_worth_to_pay'].strip())

        assert destination
        assert departure_date
        assert origin
        assert arrival_date
        assert flex_days
        assert max_worth_to_pay
        assert adult > 0 or teen > 0

        return Definition(destination, departure_date, origin, arrival_date, adult, teen, child, flex_days, max_worth_to_pay)
