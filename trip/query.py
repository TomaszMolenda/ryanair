from firebase_admin import db

from trip.dto import TripDto, FlightDto


def find_amount(fares, type_in):
    for fare in fares:
        amount = fare['amount']
        type = fare['type']
        if type == type_in:
            return amount
    return 0


def create_flights(trip):
    return_list = []
    dates = trip['dates']
    for date in dates:
        departure_date = date['departure_date']
        flights = date['flights']
        for flight in flights:
            flight_number = flight['flight_number']
            fares = flight['fares']
            adult_amount = find_amount(fares, "ADT")
            teen_amount = find_amount(fares, "TEEN")
            child_amount = find_amount(fares, "CHD")
            dto = FlightDto(departure_date, flight_number, adult_amount, teen_amount, child_amount)
            return_list.append(dto)

    return return_list


def create_dtos(trips):
    return_list = []
    for trip_id, trip in trips.items():
        checked_time = trip['date']
        trip_to_destination = trip['trip_to_destination']
        trip_to_origin = trip['trip_to_origin']

        flights_to_destination = create_flights(trip_to_destination)
        flights_to_origin = create_flights(trip_to_origin)

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
