'''
Below is a simple example of collecting twitters by using tweepy package;
The expected output should be a JSON file contains twitters you have collected
Author: Diao
'''

# import the python packages
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json
import random

# Using your your own keys and tokens to substitute the following keys and tokens 
auth = OAuthHandler('mFdyppXdtyDUy0WpsZ9C6a34J', 'IxMvhbcyZ0yHbgGZAnJvvFLxbnwWCrjaIOnmwx2lKldDwfDBCv')
auth.set_access_token('180435860-UnTc2Cx8bUxhV3bQGkLMSenTJTMkfdzzE0aJzi9w', 'Qn1p3TchyHcHCo1Sh3IdZhgeldHcgrRDlj4hdJwW2SUkn')
api = tweepy.API(auth)

print(api)


# define a class of listener

class Stdoutlistener_file_version(StreamListener):

# -----------ADD YOUR CODES HERE----------------------
    def on_data(self, data):
        with open('Collected_tweets.json', 'a', encoding='utf-8') as f:
            f.write(data)
    def on_error(self, status):
        print(status)


# create a instance of StdOutListener
stdoutlistener = Stdoutlistener_file_version()
# use the listener and auth information, we can get our own stream
stream = Stream(auth = api.auth, listener = stdoutlistener, timeout = 30.0)

print(stream)
# define the searching criteria
while True:
    try:
        # define the bouding box for your geo-search 
        Munich_boundingbox  = [11.3855, 47.9129, 11.8520, 48.2995]
        # NYC_boudingbox = [-75,40,-73,42]
        # Berlin_boudingbox = [13.0535, 52.3303, 13.7262, 52.6675]
        # Multi_cities = [-74.2589, 40.4774, -73.7004, 40.9176,-118.9448, 32.8007, -117.6462, 34.8233,11.3855, 47.9129, 11.8520, 48.2995]
       	
        
        #-------------ADD YOUR CODES HERE------------------------

        #stream.filter(track=['cartography']) # search twitter based on keywords
        stream.filter(locations = Munich_boundingbox, languages=['en,de,zh']) # searching twitters based on keywords and Geo-boudary
        break
    except Exception as e:
         # Abnormal exit: Reconnect the twitter server when 
         print('A Exception happened, sleep for 60 senconds')
         nsecs=random.randint(60,63)
         time.sleep(nsecs)
         
