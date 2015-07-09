#!/bin/sh
find . -iname '*~' -delete
cd tweet_input && find . -iname '*~' -delete
cd ..
cd tweet_output && find . -iname '*~' -delete
cd ..
cd src && find . -iname '*~' -delete
cd ..
cd sentiment_analysis && find . -iname '*~' -delete
cd ..

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/words_tweeted_clean.py

python ./src/words_tweeted_clean.py ./tweet_input/tweets.txt ./tweet_output/ft1_clean.txt
