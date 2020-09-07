import googlemaps
import pprint
import time

# Ask for authorization for info with API key
API_KEY = 'AIzaSyDYMwRSfChNGRiFY90ygxLzhiigkfBuhIo'
gmaps = googlemaps.Client(key = API_KEY)

# Variables for storing place name that user wants as well as their location
place = 'McDonalds'
my_location = '-33.8670522, 151.1957362'

# Queries for restaurants depends on delivery, takeaway, or normal
if (place == 'McDonalds delivery'):
    places_result = gmaps.places_nearby(location = my_location, keyword = place, open_now = True, rank_by = 'distance', type = 'meal_delivery')
if (place == 'McDonalds takeaway'):
    places_result = gmaps.places_nearby(location = my_location, keyword = place, open_now = True, rank_by = 'distance', type = 'meal_takeaway')

places_result = gmaps.places_nearby(location = my_location, keyword = place, open_now = True, rank_by = 'distance', type = 'restaurant')

pprint.pprint(places_result)