#!/bin/sh
find . -iname '*~' -delete
cd tweet_input && find . -iname '*~' -delete
cd ..
cd tweet_output && find . -iname '*~' -delete
cd ..
cd src && find . -iname '*~' -delete
cd .. 

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/Knowledge_Extraction.py

python ./src/Knowledge_Extraction.py ./tweet_input/tweets.txt ./tweet_output/type_tweet.txt
