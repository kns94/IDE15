#!usr/bin/python


# =================== Imports =====================================

from sys import argv
import re, math, itertools
import nltk

# =================================================================

# ==================== FUNCTIONS ==================================

def stopwordRemover(str1):
    tokens = str(str1).split()
    clnTokens = [s for s in tokens if s not in stopwordsList]
    clnstr = " ".join(clnTokens)
    return clnstr

def singleCharRemover(str2):
    tokens = str(str2).split()
    cp_tokens = tokens
    for t in tokens:
        if len(t)==1:
            cp_tokens.remove(t)
    clnstr = " ".join(cp_tokens)
    return clnstr

#Extracting word features from tweets
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

#Extracting relevant features
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

#Cleaning and splitting
def preprocess(line):

	line=re.sub('[,,.,-,!,$,%,(,),*,&,^,+,\-,",\',?,:,\;,\\\,>,<,_,=,\[,\],\\n]','',line)
	line = re.sub(r'(\s+)', ' ',line)

	#Remove Stopwords - Negative stopwords and punctuation marks have been removed from the stopword file
	line = stopwordRemover(line)	

	line=line.lower()

	#Remove single characters
	line = singleCharRemover(line)
	
	words=line.split()
	return words

# =====================END OF FUNCTIONS ============================

#Dictionary containing positive and negative tweets
pos_data=[]
neg_data=[]

#I had saved rotten tomato reviews in two seperate text files
pos_file=argv[1]
neg_file=argv[2]

stopWords_file=argv[3]
stopwordsList = [line.strip() for line in open(stopWords_file, 'r')]


print("\n\tSentiment Analysis, Brace yourselves - It's going to take some time!")
print("\n\tTraining Data (Positive Sentiments): "+pos_file)
print("\tTraining Data (Negative Sentiments): "+neg_file)

# ================================== Labeling Training Data ==========================================

for line in open(pos_file):
	
	line=re.sub('[,,.,-,!,$,%,(,),*,&,^,+,\-,",\',?,:,\;,\\\,>,<,_,=,\[,\],\\n]','',line)
	line = re.sub(r'(\s+)', ' ',line)

	#Remove Stopwords - Negative stopwords and punctuation marks have been removed from the stopword file
	line = stopwordRemover(line)

	#Remove single characters
	line = singleCharRemover(line)
	line=line.lower()
	positive_words=(line,'positive')
	pos_data.append(positive_words)

for line in open(neg_file):
	
	line=re.sub('[,,.,-,!,$,%,(,),*,&,^,+,\-,",\',?,:,\;,\\\,>,<,_,=,\[,\],\\n]','',line)
	line = re.sub(r'(\s+)', ' ',line)

	#Remove Stopwords - Negative stopwords and punctuation marks have been removed from the stopword file
	line = stopwordRemover(line)	

	line=line.lower()

	#Remove single characters
	line = singleCharRemover(line)

	negative_words=(line,'negative')
	neg_data.append(negative_words)

# =========================================================================================================

# ========================================= Tokenize ======================================================

posFeatures=[]
negFeatures=[]

#Splitting words 
for words,sentiment in pos_data:
	temp=str(words.split())
	posFeatures.append((temp,sentiment))

for words,sentiment in neg_data:
	temp=str(words.split())
	negFeatures.append((temp,sentiment))

# ===========================================================================================================

# ========================================= Classification ==================================================

#Combining Tweets
tweets = []
for (words, sentiment) in pos_data + neg_data:
    tweets.append((words.split(), sentiment))

#print(tweets)

word_features = get_word_features(get_words_in_tweets(tweets))

#Training classifier
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

print("\n\tClassifier Trained!\n")

#temp="Happy"
#word=preprocess(temp)

#print(classifier.classify(extract_features(word)))

input_file=argv[4]
output_file_name=argv[5]
output_file=open(output_file_name,'w')

print("\tTweet Input File: "+input_file)
print("\tOutput File: "+output_file_name+"\n")

for line in open(input_file):
	word=preprocess(line)
	label=classifier.classify(extract_features(word))
	#print(label)

	output_file.write(line+"    "+label)
	output_file.write("\n")

output_file.close()
