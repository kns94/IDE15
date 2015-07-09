####################################################################################################################################
#																   #
#    Additional Task 4 - Kushal Shah                          									   #	
#																   #
#    Aim: To extract entities using Alchemy API                              						           #
#																   #	
#    Input File: tweet_input/tweets.txt												   #
#    Output File: tweet_output/tweet_type.txt			                                                                   #
#                                                                                                                                  #
#    Usage: Usage: ./src/Knowledge_Extraction.py ./tweet_input/tweets.txt ./tweet_output/tweet_type.txt			           #
#																   #
#    Logic:															   #
#	   1) To traverse tweets.txt file interatively                                                                             #
#	   2) To pass values to Alchemy API						                                           #
#	   3) To edit key file if limit exceeds							                                   #
#                                                                                                                                  #
####################################################################################################################################

from alchemyapi import AlchemyAPI
import json
import sys
import re
import os

#Input File that you wish to process
input_file_name=sys.argv[1]

#print("\nInput File: "+input_file_name)

#Output File
output_file_name=sys.argv[2]

#print("Output File: "+output_file_name)

print("\n\n\tExtracting Features using Alchemy API:")
print("\n\tInput File: "+input_file_name)
print("\tOutput File: "+output_file_name+"\n")


count=0
api_name="alchemyapi"+str(count)

# Create the AlchemyAPI Object
api_name = AlchemyAPI()

outputfile=open(output_file_name,"w")

for line in open(input_file_name):
	
	#Breaking the whole line by tab
	tokens=line.strip().split("\t")
	
	#Extracting only tweets
	tweetWordStr=tokens[0]
	#print("\nTweet: "+tweetWordStr)

	#Extracting entities from Alchemy
	response = api_name.entities('text', tweetWordStr, {'sentiment': 1})

	#print(response)
	#print("count1:"+str(count))
	#print("\n")
	
	outputfile.write(tweetWordStr)

	if(response['status'] == 'OK'):
    		#print('## Response Object ##')
    		#print(json.dumps(response, indent=4))

		#print("count2:"+str(count))

		#count=count+1
    		#print('')
    		#print('## Entities ##')

		#Extracting via Alchemy API
    		for entity in response['entities']:
        		#print('text: ', entity['text'].encode('utf-8'))
        		#print('type: ', entity['type'])
        		#print('relevance: ', entity['relevance'])
        		#print('sentiment: ', entity['sentiment']['type'])

			#Entity
			text=entity['text'].encode('utf-8')
			text=text.replace("'",'')
			#print(text)
			outputfile.write("\t"+text+" ")

			#Entity Type
			etype=entity['type']
			etype=etype.replace("'",'')
			#print(etype)
			outputfile.write(etype)

        		#if 'score' in entity['sentiment']:
            		#	print('sentiment score: ' + entity['sentiment']['score'])
        		#	print('')
			#else:
    			#	print('Error in entity extraction call: ', response['statusInfo'])
	
	else:
		#print("Tweet:"+tweetWordStr)
		#print(str(response)+"\n")
		
		#In case the transaction limit exceeds; repeat the steps once again
		if "daily-transaction-limit-exceeded" in str(response):
			key=raw_input("\n\t Looks like the daily limit is exceeded, please enter new key: ")
			os.system("python alchemyapi.pyc "+key)
			os.system("sudo cp api_key.txt ../api_key.txt")
			
			print("\n")

			count=count+1

			#Renaming new API module			
			api_name="alchemyapi"+str(count)

			# Create a new AlchemyAPI Object
			api_name = AlchemyAPI()

			response = api_name.entities('text', tweetWordStr, {'sentiment': 1})
			
			#Repeating steps once again!
			if(response['status'] == 'OK'):
			 		
				for entity in response['entities']:
				
					text=entity['text'].encode('utf-8')
					text=text.replace("'",'')
					print(text)
					outputfile.write("\t"+text+"\t")

					etype=entity['type']
					etype=etype.replace("'",'')
					#print(etype)
					outputfile.write(etype)
		
	outputfile.write("\n\n")

outputfile.close()
