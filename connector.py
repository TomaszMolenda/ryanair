import requests
import database
from flight import Flight
from trip import Trip


def find_flight(data, flight_date):
    currency = data['currency']
    for trip in data['trips']:
        for date in trip['dates']:
            if flight_date in date['dateOut']:
                for flight in date['flights']:
                    child_amount = ''
                    teen_amount = ''
                    adult_amount = ''
                    for fare in flight['regularFare']['fares']:
                        if fare['type'] == 'CHD':
                            child_amount = fare['amount']
                        if fare['type'] == 'TEEN':
                            teen_amount = fare['amount']
                        if fare['type'] == 'ADT':
                            adult_amount = fare['amount']
                    origin_name = trip['originName']
                    destination_name = trip['destinationName']
                    return Flight(currency, origin_name, destination_name, child_amount, teen_amount, adult_amount)


def check():

    date_in = database.Database.getInstance().date_in
    date_out = database.Database.getInstance().date_out
    destination = database.Database.getInstance().destination
    origin = database.Database.getInstance().origin

    params = {
        'ADT': 3,
        'CHD': 2,
        'TEEN': 1,
        'DateOut': date_out,
        'DateIn': date_in,
        'Origin': origin,
        'Destination': destination,
        'FlexDaysIn': 6,
        'FlexDaysOut': 2,
        'INF': 0,
        'IncludeConnectingFlights': 'true',
        'RoundTrip': 'true',
        'ToUs': 'AGREED',
        'exists': 'false',
        'promoCode': ''
    }

    resp = requests.get("https://desktopapps.ryanair.com/v4/pl-pl/availability/", params=params)
    data = resp.json()

    flight_to_destination = find_flight(data, date_out)
    flight_from_origin = find_flight(data, date_in)

    database.Database.getInstance().trip = Trip(flight_to_destination, flight_from_origin)

    pass
