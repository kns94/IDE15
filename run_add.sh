#!/bin/sh
find . -iname '*~' -delete
cd tweet_input && find . -iname '*~' -delete
cd ..
cd tweet_output && find . -iname '*~' -delete
cd ..
cd src && find . -iname '*~' -delete
cd ..
python ./src/words_tweeted_add.py ./tweet_input/tweets.txt ./tweet_output/ft1_add.txt
python ./src/median_unique_add.py ./tweet_input/tweets.txt ./tweet_output/ft2_add.txt

