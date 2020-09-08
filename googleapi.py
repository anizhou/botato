import googlemaps
import pprint
import time

# Ask for authorization for info with API key
API_KEY = 'AIzaSyDYMwRSfChNGRiFY90ygxLzhiigkfBuhIo'
gmaps = googlemaps.Client(key = API_KEY)

def top_five(location, place): #should pass location and food

    # Make a request for nearby places near user's location
    places_result = gmaps.places_nearby(location = location, keyword = place, open_now = True, rank_by = 'distance', type = 'restaurant, cafe')   

    # List to store top five results
    five_list = []

    if len(places_result['results']) > 5:
        for i in range(5):

            # Define place id
            my_place_id = places_result['results'][i]['place_id']

            # Define necessary fields
            my_fields = ['name', 'formatted_phone_number', 'price_level', 'rating']

            # Make a request for the place details
            place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

            five_list.append(place_details)

    elif (len(places_result['results']) <= 5):
        for place in places_result['results']:

            my_place_id = place['place_id']    
            my_fields = ['name', 'formatted_phone_number', 'price_level', 'rating']
            place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
            five_list.append(place_details)
    
    return five_list


#top_five('32.9858, -96.7501', "tea")
# top_five('40.711070,-73.803520',"Mcdonalds")
print(top_five('40.7828514,-73.96528127819182',"tea"))