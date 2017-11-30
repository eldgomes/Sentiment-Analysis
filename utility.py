#******************************************************************
#Module to clean JSON objects fetched from streaming API and 
#to get count of total tweets and count of each class of polarity
#******************************************************************

import sys, json, csv, time, matplotlib.dates, os
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import textProcessor as TP

#returns the count of positive, neutral, negative tweets
def getPosNegNeutTot():
	df=pd.read_csv("tweetpolarity.csv",header=None)
	data=df.values
	polarity=[]
	positive=0
	negative=0
	neutral=0
	for row in data:
		polarity.append(row[1])
	for i in polarity:
		if i==1:
			positive+=1
		elif i==0:
			neutral+=1
		elif i==-1:
			negative+=1
			
	return positive,neutral,negative

#fetch the required data from JSON objects and save in a temporary csv file
def savePolarity(filename):
	try:
		os.remove("tweetpolarity.csv")
	except OSError:
		pass	
	
	with open(filename) as openfileobject:
		for line in openfileobject:
			line = line.strip()
			if not line:
				continue
			else:
				try:	
					parsed_json = json.loads(line)
					text=parsed_json['text'].encode("utf-8")
					lang=parsed_json['lang'].encode("utf-8")
					date=parsed_json['created_at'].encode("utf-8")
					if lang=='en':
						print(text)
						x=TP.getSentiment(text)
						f = csv.writer(open("tweetpolarity.csv","a"))
						f.writerow((text,x,date))
				except KeyError:
					continue

#returns the total number of tweets fetched					
def getAllTweetCount(filename):
	i=0
	with open(filename) as openfileobject:
		for line in openfileobject:
			line = line.strip()
			if not line:
				continue
			else:
				pass
			i+=1
	return i