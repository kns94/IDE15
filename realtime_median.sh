#!/bin/sh
find . -iname '*~' -delete
cd tweet_input && find . -iname '*~' -delete
cd ..
cd tweet_output && find . -iname '*~' -delete
cd ..
cd src && find . -iname '*~' -delete
cd .. 

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/realtime_median.py

python ./src/realtime_median.py ./tweet_input/tweets_download.txt ./tweet_output/realtime_median.txt 
