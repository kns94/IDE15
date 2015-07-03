####################################################################################################################################
#																   #
#    Task2- Kushal Shah														   #	
#																   #
#    Aim: To calculate median of unique words in a particular data-set   						           #
#																   #	
#    Input File: tweet_input/tweets.txt												   #
#    Output File: tweet_output/ft2.txt 				                                                                   #
#                                                                                                                                  #
#    Usage: python words_tweeted.py                                                                                                #
#																   #
#    Logic:															   #
#	   1) To traverse tweets.txt file interatively                                                                             #
#	   2) To split text by a space ' ' and to add unique tokens to a list                                                      #
#	   3) To calculate mean accordingly                                                                                        #
#                                                                                                                                  #
####################################################################################################################################

import operator
import os

#Change directory - Go to parent directory
os.chdir('..')

#Save path of parent directory
path=os.getcwd()

#Input File containing tweets
tweet_file_raw="tweet_input/tweets.txt"

#Complete path of the file
tweet_file=path+"/"+tweet_file_raw

#Dictionary of mean
mean={}

count=0

#Traversing tweets line by line
for line in open(tweet_file):
	
	#print(line)

	#List containing unique keywords
	unique_list=[]

	#Seperating words by space
	tweetWords=line.strip().split(' ')
		
	i=0

	while(i<len(tweetWords)):

		if(tweetWords[i]):
			#Appending unique keywords in a list
			if(tweetWords[i] not in unique_list):
				unique_list.append(tweetWords[i])
		
			#print(tweetWords[i]+"\n")

		i=i+1

	#Calculating mean by multiplying previous mean by number of values; adding latest value and dividing by new count
	if(count!=0):
		mean[count]=((mean[count-1]*(count))+len(unique_list))/float(count+1)
	else:
		#Mean of first value is the value itself
		mean[count]=len(unique_list)

	count=count+1	

#print(mean)

#Output File Name
output_file_name_raw="tweet_output/ft2.txt"

#Complete Output File Name
output_file_name=path+"/"+output_file_name_raw

output_file=open(output_file_name,'w')

#Saving latest values of mean in a file

i=0
while(i<len(mean)):
	output_file.write(str(mean[i]))
	output_file.write("\n")
	i=i+1

output_file.close()
