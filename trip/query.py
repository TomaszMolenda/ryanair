from firebase_admin import db

from trip.dto import TripDto, FlightDto


def create_flights(flights):
    return_list = []
    for flight in flights:
        date = flight['date']
        flight_number = flight['flight_number']
        adult_amount = flight['adult_amount']
        teen_amount = flight['teen_amount']
        child_amount = flight['child_amount']
        dto = FlightDto(date, flight_number, adult_amount, teen_amount, child_amount)
        return_list.append(dto)

    return return_list


def create_dtos(trips):
    return_list = []
    for trip_id, trip in trips.items():
        checked_time = trip['date']

        flights_to_destination = create_flights(trip['flights_to_destination'])
        flights_to_origin = create_flights(trip['flights_to_origin'])

        dto = TripDto(checked_time, flights_to_destination, flights_to_origin)

        return_list.append(dto)

    return return_list


class TripQuery:
    __instance = None

    @staticmethod
    def get_instance():
        if TripQuery.__instance is None:
            TripQuery()
        return TripQuery.__instance

    def __init__(self):
        if TripQuery.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TripQuery.__instance = self

    @staticmethod
    def list_by_definition_id(definition_id):
        trips = db.reference().child('trips').child(definition_id).get()

        if trips is None:
            return []

        return create_dtos(trips)
