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
        self.trip = None
        self.date_out = '2020-02-15'
        self.date_in = '2020-02-29'
        self.destination = None  # 'TFS'
        self.origin = None  # 'SXF'
