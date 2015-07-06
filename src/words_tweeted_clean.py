####################################################################################################################################
#																   #
#    Additional Task 2 - Kushal Shah                          									   #	
#																   #
#    Aim: To calculate frequency of a particular words in a given data-set and to remove additional characters 		           #
#																   #	
#    Input File: tweet_input/tweets.txt												   #
#    Output File: tweet_output/ft1_clean.txt			                                                                   #
#                                                                                                                                  #
#    Usage: python ./src/words_tweeted_clean.py ./tweet_input/tweets.txt ./tweet_output/ft1_clean.txt                              #
#																   #
#    Logic:															   #
#	   1) To traverse tweets.txt file interatively                                                                             #
#	   2) To split text by a space ' ' and remove additional characters                                                        #
#	   3) To check if the value exists in the dictionary and to increment count accordingly                                    #
#                                                                                                                                  #
####################################################################################################################################

import operator
from sys import argv
import re

#I had intended to use OS library; but will edit it given David's recent update!

#import os

#Change directory - Go to parent directory
#os.chdir('..')

#Save path of parent directory
#path=os.getcwd()

#Input File containing tweets
#tweet_file_raw="tweet_input/tweets.txt"

#Complete path of the file
#tweet_file=path+"/"+tweet_file_raw

tweet_file=argv[1]

#Dictionary of unique keywords
words={}

#Traversing tweets line by line
for line in open(tweet_file):
	
	#print(line)

	#Seperating words by space
	tweetWords=line.strip().split(' ')
		
	i=0

	while(i<len(tweetWords)):

		#Making sure that all the key words are converted to lower case and removing stopwords
		tweetWords[i]=re.sub('[,,.,-,!,$,%,(,),*,&,^,+,\-,",\',?,:,\;,\\\,>,<,_,=,\[,\]]',' ',tweetWords[i])
		tweetWords[i]=tweetWords[i].replace(' ','')
		tweetWords[i]=tweetWords[i].lower()

		#Appending words in dictionary and incrementing count 

		if(tweetWords[i]):
			if(tweetWords[i] not in words):
				words[tweetWords[i]]=1
			else:
				words[tweetWords[i]]=words[tweetWords[i]]+1

		#print(tweetWords[i]+"\n")

		i=i+1

#sorting words according to ASCII sequence
sorted_words=sorted(words.items(),key=operator.itemgetter(0))

#Output File Name
#output_file_name_raw="tweet_output/ft1.txt"

#Complete Output File Name
#output_file_name=path+"/"+output_file_name_raw

output_file_name=argv[2]

output_file=open(output_file_name,'w')

#Saving dictionary in a file
for tokens, count in sorted_words:
	output_file.write(tokens+"\t")
	output_file.write(str(count))
	output_file.write("\n")

output_file.close()
