import googlemaps
import pprint
import time

# Ask for authorization for info with API key
API_KEY = 'AIzaSyDYMwRSfChNGRiFY90ygxLzhiigkfBuhIo'
gmaps = googlemaps.Client(key = API_KEY)

# Variables for storing place name that user wants as well as their location
place = 'McDonalds delivery'
my_location = '-33.8670522, 151.1957362'

# Make a request for nearby places near user's location
places_result = gmaps.places_nearby(location = my_location, keyword = place, open_now = True, rank_by = 'distance', type = 'restaurant')

# Loop through all the places in the results
for place in places_result['results']:

    # Define place id
    my_place_id = place['place_id']

    # Define necessary fields
    my_fields = ['name', 'formatted_phone_number', 'price_level', 'rating']

    # Make a request for the place details
    place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

    print(place_details)