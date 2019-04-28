class Database:
    __instance = None
    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self
        self.checked_trips = []
        self.trip_to_destination = None
        self.trip_to_origin = None
        self.departure_date = None  # '2020-02-15'
        self.arrival_date = None  # '2020-02-29'
        self.destination = None  # 'TFS'
        self.origin = None  # 'SXF'
        self.adult = None
        self.teen = None
        self.child = None
        self.flex_days = None

    def add_checked_trip(self, checked_trip):
        self.checked_trips.append(checked_trip)
        pass
