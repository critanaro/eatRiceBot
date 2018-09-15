#Python libraries that we need to import for our bot
from flask import Flask, request
from pymessenger.bot import Bot
from __future__ import print_function
import random
import sys
import os 

app = Flask(__name__) ## This is how we create an instance of the Flask class for our app

ACCESS_TOKEN = 'EAAKMgA79MiwBAJpvCa0fOiEhkuHux94c7dwgzOZCvGR8f0pxoZB5csi3o6rPkZAd30MRGmogLHMuF409B954pDl3EgITLzn0qmn5TLlSUEOobdvUZBT1ZCJT2BvYzlYGhrJLQRi6xUd0ZCjyRC75uhhk1lcH1WZCmvy7ZC2TQOhx3dyJyA8yGlme'   #ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = 'TESTINGTOKEN' ## Replace 'VERIFY_TOKEN' with your verify token
bot = Bot(ACCESS_TOKEN) ## Create an instance of the bot

def verify_fb_token(token_sent):
    ## Verifies that the token sent by Facebook matches the token sent locally
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# Chooses a message to send to the user
def get_message_text(input_text):
    greeting = firstEntity(message.nlp, 'greetings');
    if (greeting && greeting.confidence > 0.8):
        return "Hi! This is identified as a greeting by built in NLP"
    else:
        return "Hack on!"

# Checks whether the first entitiy is name or not
def firstEntity(nlp, name):
    return nlp and nlp['entities'] and nlp['entities']['name'] and nlp['entities']['name'][0]

## Send text message to recipient
def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response) ## Sends the 'response' parameter to the user
    return "Message sent"

## This endpoint will receive messages 
@app.route("/", methods=['GET', 'POST'])
def receive_message():

    ## Handle GET requests
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token") ## Facebook requires a verify token when receiving messages
        return verify_fb_token(token_sent)

    ## Handle POST requests
    else: 
       output = request.get_json() ## get whatever message a user sent the bot
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id'] ## Facebook Messenger ID for user so we know where to send response back to

                test_message = message['message'].get('text')
                response_sent_text = get_message_text(test_message)
                send_message(recipient_id, response_sent_text)

    return "Message Processed"

## Ensures that the below code is only evaluated when the file is executed, and ignored if the file is imported
if __name__ == "__main__": 
    app.run() ## Runs application
