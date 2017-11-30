#**************************************************************
#Module to handle tweet text cleaning and text classification
#**************************************************************

import re
from textblob import TextBlob

#Removes mentions, special characters and URLs from tweet text
def clean_tweet(tweet):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#Function to classify tweet polarity.
def getSentiment(text):
	temp=clean_tweet(text)
	print temp
	analysis = TextBlob(temp)
	if analysis.sentiment.polarity > 0: #positive
		return 1
	elif analysis.sentiment.polarity == 0: #neutral
		return 0
	else: #negative
		return -1