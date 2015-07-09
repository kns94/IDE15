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
chmod a+x ./sentiment_analysis/sentiment_analysis.py

python ./sentiment_analysis/sentiment_analysis.py ./sentiment_analysis/trainingData_positive.txt ./sentiment_analysis/trainingData_negative.txt ./sentiment_analysis/stopWords.txt ./tweet_input/tweets.txt ./tweet_output/sentiment.txt
