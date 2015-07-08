####################################################################################################################################
#																   #
#    Additional Task 3 - Kushal													   #	
#																   #
#    Aim: To download tweets using Twitter API and to calculate median instantaneously					           #
#																   #	
#    Output File:  ./tweet_input/tweets_download.txt ./tweet_output/realtime_median.txt                                            #
#                                                                                                                                  #
#    Usage: python realtime_median.py ./tweet_input/tweets_download.txt ./tweet_output/realtime_median.txt                         #
#																   #
#    Logic:															   #
#	   1) To download tweets using Tweepy API and to calculate median instantaneously                                          #
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

#This listener will extract tweets and calculate median of unique words!
class StdOutListener(StreamListener):
   
    print("\n")

    def on_data(self, data):

        global count
	global mean

        tweet=json.loads(data)
	#tweet_asc=repr(tweet["text"])
	
	#Extracting just the tweet text
	tweet=tweet["text"]
	tweet=tweet.encode("UTF-8")

	#Unicode Encoder
	print("\n"+str(tweet))

	output_file.write(str(tweet))
	output_file.write("\n")

        #List containing unique keywords
	unique_list=[]

	#Seperating words by space
	tweetWords=tweet.strip().split(' ')

        i=0

	while(i<len(tweetWords)):

		if(tweetWords[i]):
			#Appending unique keywords in a list
			if(tweetWords[i] not in unique_list):
				unique_list.append(tweetWords[i])
		
			#print("\n"+str(tweetWords[i])+"\n")

		i=i+1

        #print("\n\n"+str(unique_list)+"\n\n\n")

	#Calculating mean by multiplying previous mean by number of values; adding latest value and dividing by new count
	if(count!=0):
		mean[count]=((mean[count-1]*(count))+len(unique_list))/float(count+1)
		
	else:
		#Mean of first value is the value itself
		mean[count]=len(unique_list)
		
		
	mean_file.write(str("%.2f" % mean[i]))
	mean_file.write("\n")

	count=count+1	     

        return True

    def on_error(self, status):
        print status
	print("\n")

if __name__ == '__main__':

    #Saving tweets in outputfile
    output_file_name=argv[1]
    output_file=open(output_file_name,'w')

    #Saving median in another outputfile
    mean_file_name=argv[2]
    mean_file=open(mean_file_name,'w')

    #Dictionary containing median of unique keywords in a tweet
    mean={}

    count=0

    print("\n\tPress Ctrl+C to stop tweet extraction!\n\n")
    time.sleep(3)
 
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'data'
    stream.filter(track=['data'])
