import googlemaps
import pprint
import time
from geopy.geocoders import Nominatim

# Ask for authorization for info with API key
API_KEY = 'AIzaSyDYMwRSfChNGRiFY90ygxLzhiigkfBuhIo'
gmaps = googlemaps.Client(key = API_KEY)

geolocator = Nominatim(user_agent="googleapi")
#user_input=input("Input location: ")
#location = geolocator.geocode(user_input)

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
            my_fields = ['name', 'formatted_address', 'formatted_phone_number', 'price_level', 'rating']

            # Make a request for the place details
            place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

            five_list.append(place_details)

    elif (len(places_result['results']) <= 5 and len(places_result['results'])>0):
        for place in places_result['results']:

            my_place_id = place['place_id']    
            my_fields = ['name', 'formatted_address', 'formatted_phone_number', 'price_level', 'rating']
            place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
            five_list.append(place_details)
    elif (len(places_result['results'])==0):
        return "Place is closed"
    
    results = ""
    for item in five_list:
        results += "{name}\n {address}\n Number: {phone_number}\n Rating: {rating}\n\n".format(name = item['result']['name'],address=item['result']['formatted_address'],phone_number = item['result']['formatted_phone_number'], rating = item['result']['rating']) 

    return results


#latt = str(location.latitude)
#lon = str(location.longitude)
#g = latt + ',' + lon

#food_choice=input("Enter choice: ")
#choice=top_five(g, food_choice)  
#print(choice)  

def get_location(foodie):
	foodie=geolocator.geocode(foodie)
	lat=str(foodie.latitude)
	lon=str(foodie.longitude)
	address=lat+','+lon
	return address

food = '159 jamaica avenue'

print(get_location(food))