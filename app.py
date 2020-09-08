from flask import Flask, request
from flask_ngrok import run_with_ngrok
import requests, googleapi
from geopy.geocoders import Nominatim


app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

# Tokens
FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'bob'
PAGE_ACCESS_TOKEN = 'EAAE361oDiy4BAG23yqgcoMO5hmu7v4EEM55HNbWgdrDAdDGAYvuu9NpnjANm2aYDFmC5VZAEMSGaFZBZBFMYsWVKw67006NJjx6xJ1mnneoZCawFWWDHKyPwNQjQhnviDqZBGU7xhBmeZBVXk5Q5auVzZBeFMw0G00kHTmBjtOiSQZDZD'
PAGE_ACCESS_TOKEN_CAT='EAAIiC9PUCssBAOK8ZAXbZBapxfBU2hZA1UUVzJwV9kFGPd5kJCxXIYMHu771nWSLmj60USfnRIOKhZCeVeyX7HsQYj2ZB8Jm5IRVbrY3B3LQPT7ZBLrpjXKTUfWJn7uotQYCBIa3RA4nyyTMVDJcI0sCrxGhX3AA2mqfRsfQDAZBwZDZD'

@app.route("/")
def home():
    return "Howdy, Flask!"

# Get the bot response
geolocator = Nominatim(user_agent="googleapi")


def get_location(address):
	address=geolocator.geocode(str(address))
	latt=str(address.latitude)
	lon=str(location.longitude)
	address=latt+','+lon
	return address

def get_bot_response(location,message):

    return googleapi.top_five(location, message)

# Verify whether webhook is connected
def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

# Formulate a response to the user and pass it to the function that sends it
def respond(sender, message):
	response = get_bot_response(address,message)
	send_message(sender, response)

# Check if the message is a message from the user
def is_user_message(message):
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))

# Main function flask uses to listen at the "/webhook" endpoint
@app.route("/webhook", methods=['GET', 'POST'])
def listen():
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text)

        return "ok"

# Send a response back to the user
def send_message(recipient_id, text):
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN_CAT
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json()

if __name__ == '__main__':
    app.run()