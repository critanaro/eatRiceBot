#Python libraries that we need to import for our bot
from __future__ import print_function
from flask import Flask, request
from pymessenger.bot import Bot
import random
import sys
import os 
import json
import csv

from wit import Wit
access_token = "GGDBZAV5X6J5CJBCKOOLWWWMMMMSHTHR"
wit_client = Wit(access_token)

app = Flask(__name__) ## This is how we create an instance of the Flask class for our app

ACCESS_TOKEN = 'EAAKMgA79MiwBAJpvCa0fOiEhkuHux94c7dwgzOZCvGR8f0pxoZB5csi3o6rPkZAd30MRGmogLHMuF409B954pDl3EgITLzn0qmn5TLlSUEOobdvUZBT1ZCJT2BvYzlYGhrJLQRi6xUd0ZCjyRC75uhhk1lcH1WZCmvy7ZC2TQOhx3dyJyA8yGlme'   #ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = 'TESTINGTOKEN' ## Replace 'VERIFY_TOKEN' with your verify token
bot = Bot(ACCESS_TOKEN) ## Create an instance of the bot

HELP_MESSAGE = "I can provide information about dining options, allergies, and schedules here at Rice!"
EXAMPLES = ["what can I eat at West?", "where can I find vegetarian food?", "which serveries are open today?"]

def help_statement():
    return HELP_MESSAGE + " Ask me a question like \"" + random.choice(EXAMPLES) + "\""

def verify_fb_token(token_sent):
    ## Verifies that the token sent by Facebook matches the token sent locally
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# Chooses a message to send to the user
def get_response_text(message):
    message_text = message['text']

    response_message = ""

    nlp_response = wit_client.message(message_text)

    with open('nlp_response_wit.txt', 'w') as file:
        file.write(json.dumps(nlp_response))

    if ('entities' in nlp_response):

        nlp_entities = nlp_response['entities']

        EATERIES = ["west", "north", "south", "seibel", "sid", "baker"]

        if ('eating' in nlp_entities):
            #response_message += "I am " + str(round(nlp_entities['eating'][0]['confidence'] * 100)) + \
            #                    "% confident you are talking about eating\n"
            
            # If the user provided no information other than indication that they are talking about eating
            if len(nlp_entities) == 1:
                response_message = "It seems like you're interested in eating. " + help_statement()

        if ('serveries' in nlp_entities and nlp_entities['serveries'][0]['confidence'] > .7):
            #response_message += "I am " + str(round(nlp_entities['serveries'][0]['confidence'] * 100)) + \
            #                    "% confident you are talking about serveries\n"

            entity = nlp_entities['serveries'][0]
            servery = entity['value']
            if servery is 
            is_open()

        if ('mealtype' in nlp_entities):
            response_message += "I am " + str(round(nlp_entities['mealtype'][0]['confidence'] * 100)) + \
                                "% confident you are talking about meals\n"

        if ('schedule' in nlp_entities):
            response_message += "I am " + str(round(nlp_entities['schedule'][0]['confidence'] * 100)) + \
                                "% confident you are talking about schedules\n"

        if ('datetime' in nlp_entities):
            response_message += "I am " + str(round(nlp_entities['datetime'][0]['confidence'] * 100)) + \
                                "% confident you are talking about dates and times\n"

        if ('foodtype' in nlp_entities):
            response_message += "I am " + str(round(nlp_entities['foodtype'][0]['confidence'] * 100)) + \
                                "% confident you are talking about foods\n"

        if ('dietary' in nlp_entities):
            response_message += "I am " + str(round(nlp_entities['dietary'][0]['confidence'] * 100)) + \
                                "% confident you are talking about dietary restrictions\n"

    if not response_message:
        response_message = "I don't understand that statement. " + help_statement()

    return response_message
    """
    entity1 = firstEntity(message['nlp'])
    if (entity1 and 'greeting' in entity1):
        return "Hi! This is identified as a greeting by built in NLP"
    elif (entity1 and 'sentiment' in entity1):
        return "This is a sentiment, as defined by NLP"
    else:
        return "Hack on!"
    """

"""
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
"""

# Checks whether the first entitiy is 'name' or not
def firstEntity(nlp):
    if nlp and 'entities' in nlp:
        return nlp['entities']
    else:
        return False

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
        with open('json_in_message.txt', 'w') as outfile:
            json.dump(output, outfile)

        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id'] ## Facebook Messenger ID for user so we know where to send response back to

                    response_text = get_response_text(message['message'])
                    send_message(recipient_id, response_text)

        return "Message Processed"

## Ensures that the below code is only evaluated when the file is executed, and ignored if the file is imported
if __name__ == "__main__": 
    app.run() ## Runs application
