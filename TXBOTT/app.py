#Python libraries that we need to import for our bot
from __future__ import print_function
import random, sys
from flask import Flask, request
from pymessenger.bot import Bot

import os 

app = Flask(__name__)
ACCESS_TOKEN = 'EAAKMgA79MiwBAJpvCa0fOiEhkuHux94c7dwgzOZCvGR8f0pxoZB5csi3o6rPkZAd30MRGmogLHMuF409B954pDl3EgITLzn0qmn5TLlSUEOobdvUZBT1ZCJT2BvYzlYGhrJLQRi6xUd0ZCjyRC75uhhk1lcH1WZCmvy7ZC2TQOhx3dyJyA8yGlme'   #ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = 'TESTINGTOKEN'   #VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot (ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                #testing out built-in NLP

                greeting = message.nlp and nlp.entities and nlp.entitites['greetings'] and nlp.entities[name][0]
                if message['message'].get('text'):
                    if (greeting and (greeting.confidence>0.8)):
                        response_sent_text = get_message()
                    else:
                        response_sent_text = "fuck"
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a message to send to the user based on entity values
def get_message():
    response = "Hello there"
    # return selected item to the user
    return response

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)




if __name__ == "__main__":
    app.run()
