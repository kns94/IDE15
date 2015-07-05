### Term Frequency and Mean Calculation
Note: The following program was written on Ubuntu 12.04 using Python 2.7.3, GCC - 4.6.3. It should work on other systems, but in case it doesn't - Please feel free to reach out to me; *we'll* make it work!

###### Instructions to Run

1. Run the shell script `./run.sh` on your terminal; it will execute two python files - `/src/median_unique.py` and `/src/words_tweeted.py`

2. I had added some additional features apart for the task:

    1. To download tweets using twitter API; Run the script `tweet_download.sh` - It will download tweets in the file `/tweet_input/tweets.txt`. You'll have to ask me for the app secret! But, please run the script `install.sh` to install additional libraries; make sure that you have root access :)

    2. Please execute the shell script - run the shell script `./run_add.sh` on your terminal; it will execute two python files - `/src/median_unique_add.py` and `/src/words_tweeted_add.py` 

###### Introduction

I would like to thank David and the entire team at Insight for giving me this opportunity to show-case my knowledge base. 

The first challenge is known as [Term Frequency and Weighting](http://nlp.stanford.edu/IR-book/html/htmledition/term-frequency-and-weighting-1.html) It's a fairly common concept used while analyzing Natural Language; mainly used to conceptualize how significant a particular word is and if it is not, then to *discard* it - so that we can focus only on **relevant** keywords. Here, we assume each line as a document; so we are calculating words common in different documents in a particular data-set.

Second challenge seems more in the lines to test programming abilities

###### Problem

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of unique words per tweet, and update this median as tweets come in.

###### Implementation

**Test Data-Set:** Tweets extracted using [Twitris 2.0](http://knoesis.org/projects/twitris) by entering specific keywords pertaining to Gender-Based Violence. The data-set is saved in the file named `tweets_gbv.txt`. You would be required to change input file in `run.sh` and `run_advanced.sh` accordingly; or you can *rename* the file as `tweets.txt`.

**Programming Specifics:** Programmed on Ubuntu 12.04 using Python 2.7.3

The problem was easy; but my focus was to reduce both space and time complexity in case we encounter a very large file. So, I was confused between NdArray and Dictionary. But, since I did not knew the size of my array - It was better to use a dictionary in this case. Moreover dictionary uses a Hash Table; so it will while incrementing the count.

Now, I split the keywords by a blank space and then appended tokens to my dictionary; I then incremented count accordingly. Next step was to sort the keywords according to ASCII feature and then I printed the output to file. 

For the second task, I extracted unique keywords for a particular tweet and saved it in a dictionary. I then calculated mean by multiplying previous mean by number of values - adding latest value and dividing the sum by new count

###### Additional Features Implemented [To be added iteratively]

1. Tweets will be automatically extracted after every-run \[Done]
2. The characters in tweet.txt need not be of lower-case; the system will convert every word/character to lower-case and process accordingly \[Done]
3. Punctuations will be removed \[Done]
4. Output File will contain analysis about the type of Keyword
5. Median will be calculated as line arrives

###### Constraints

The code works on every test case effeciently. Yes, ofcourse a blank file will produce an equivalent output! 
I will check for boundary cases and update accordingly. 

###### Parting Comments

It was a great learning experience, while solving this challenge. I hope that I will get an opportunity to solve such interesting problems in the near future. In case you would like to suggest me something or need further interpration; please feel free to reach out to me at kushalns5@gmail.com. Looking forward to interacting and learning from you!
