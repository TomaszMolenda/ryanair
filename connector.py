import requests
from firebase_admin import db

from email_service import EmailApplicationService
from entity import Flight, CheckedTrip
from trip.query import TripQuery


def find_amount(fares, type_in):
    for fare in fares:
        amount = fare['amount']
        type = fare['type']
        if type == type_in:
            return amount
    return 0


def find_flights(data, _from, _to):
    return_list = []

    for trip in data['trips']:
        if _from in trip['origin'] and _to in trip['destination']:
            for date in trip['dates']:
                if len(date['flights']) > 0:
                    flight_date = date['dateOut']
                    for flight in date['flights']:
                        fares = flight['regularFare']['fares']
                        adult_amount = find_amount(fares, "ADT")
                        teen_amount = find_amount(fares, "TEEN")
                        child_amount = find_amount(fares, "CHD")
                        flight = Flight(flight_date, flight['flightNumber'], adult_amount, teen_amount, child_amount)
                        return_list.append(flight)
    return return_list


def check(definition_id, definition):

    departure_date = definition.departure_date
    arrival_date = definition.arrival_date
    destination = definition.destination
    origin = definition.origin
    adult = definition.adult
    teen = definition.teen
    child = definition.child
    flex_days = definition.flex_days

    params = {
        'ADT': adult,
        'CHD': child,
        'TEEN': teen,
        'DateOut': departure_date,
        'DateIn': arrival_date,
        'Origin': origin,
        'Destination': destination,
        'FlexDaysIn': flex_days,
        'FlexDaysOut': flex_days,
        'INF': 0,
        'IncludeConnectingFlights': 'true',
        'RoundTrip': 'true',
        'ToUs': 'AGREED',
        'exists': 'false',
        'promoCode': ''
    }

    resp = requests.get("https://desktopapps.ryanair.com/v4/pl-pl/availability/", params=params)
    data = resp.json()

    flights_to_destination = find_flights(data, _from=origin, _to=destination)
    flights_to_origin = find_flights(data, _from=destination, _to=origin)

    checked_trip = CheckedTrip(flights_to_destination, flights_to_origin)

    trip_query = TripQuery.get_instance()
    persisted_trips = trip_query.list_by_definition(definition)

    checked_trip.remove_existing(persisted_trips)

    if checked_trip.flights_to_origin or checked_trip.flights_to_destination:
        db.reference().child('trips').child(definition_id).push(checked_trip.asdict())
        application_service = EmailApplicationService.get_instance()
        application_service.send_email('mamammaam')
    pass
