import requests
import database
from entity import Fare, Flight, Trip, Date, CheckedTrip


def find_trip(data, _from, _to):
    currency = data['currency']
    for trip in data['trips']:
        if _from in trip['origin'] and _to in trip['destination']:
            dates = []
            for date in trip['dates']:
                if len(date['flights']) > 0:
                    flights = []
                    flight_date = date['dateOut']
                    for flight in date['flights']:
                        fares = []
                        for fare in flight['regularFare']['fares']:
                            fares.append(Fare(fare['type'], fare['amount'], currency))
                        flights.append(Flight(flight['flightNumber'], fares))
                    dates.append(Date(flight_date, flights))
            return Trip(trip['origin'], trip['destination'], dates)


def check():

    departure_date = database.Database.getInstance().departure_date
    arrival_date = database.Database.getInstance().arrival_date
    destination = database.Database.getInstance().destination
    origin = database.Database.getInstance().origin
    adult = database.Database.getInstance().adult
    teen = database.Database.getInstance().teen
    child = database.Database.getInstance().child
    flex_days = database.Database.getInstance().flex_days

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

    trip_to_destination = find_trip(data, _from=origin, _to=destination)
    trip_to_origin = find_trip(data, _from=destination, _to=origin)

    checked_trip = CheckedTrip(trip_to_destination, trip_to_origin)

    database.Database.getInstance().add_checked_trip(checked_trip)

    pass
