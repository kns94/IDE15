####################################################################################################################################
#																   #
#    Kushal Shah														   #	
#																   #
#    Aim: To download tweets using Twitter API                           						           #
#																   #	
#    Output File: tweet_input/tweets.txt			                                                                   #
#                                                                                                                                  #
#    Usage: python tweet_download.py ./tweet_input/tweets.txt                                                                      #
#																   #
#    Logic:															   #
#	   1) To download tweets using Tweepy API                                                                                  #
#                                                                                                                                  #
####################################################################################################################################


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
from sys import argv
#import codecs
import time

#Variables that contain user credentials to Twitter API
access_token="Your access token"
access_token_secret="Secret of access token"
consumer_key="Your consumer key"
consumer_secret="Consumer Key secret"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
   
    print("\n")

    def on_data(self, data):
        tweet=json.loads(data)
	#tweet_asc=repr(tweet["text"])
	
	#Extracting just the tweet text
	tweet=tweet["text"]

	#Unicode Encoder
	print(str(tweet.encode("UTF-8")))

	output_file.write(str(tweet.encode("UTF-8")))
	output_file.write("\n")
        return True

    def on_error(self, status):
        print status
	print("\n")

if __name__ == '__main__':

    #Saving tweets in outputfile
    output_file_name=argv[1]
    output_file=open(output_file_name,'w')

    print("\n\tPress Ctrl+C to stop tweet extraction!\n\n")
    time.sleep(3)
 
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'data'
    stream.filter(track=['data'])
