#**************************************************************
#Module containing driving function to call classifier 
#and choose the type of visualization. 
#**************************************************************

import sys, json, select, csv, time, matplotlib.dates, graphic, utility
import matplotlib.pyplot as plt
import numpy as np
import textProcessor as TP
import pandas as pd 
import numpy as np 
 
def main():
	keyword=raw_input("Enter the Keyword: ")
	filename=raw_input("Enter the datastore name(as .csv): ")

	utility.savePolarity(filename)

	print("\nSELECT OPTION")
	print("1) Sentiments in Percentage")
	print("2) Sentiments in Numbers")
	print("3) Time Chart")
	print("4) Sentiment Timeline")
	print("5) Exit\n")

	i=utility.getAllTweetCount(filename)
	positive,neutral,negative=utility.getPosNegNeutTot()

	num=0
	while True:
		choice = raw_input("Enter Choice: ")
		num=int(choice)
		if num==1:
			graphic.pie_chart(positive,negative,neutral,i,keyword)
		elif num==2:
			graphic.bar_charts(positive,negative,neutral,i,keyword)
		elif num==3:
			graphic.timeChart(keyword)
		elif num==4:
			graphic.multilineChart(keyword)
		elif num==5:
			sys.exit()
		else:
			print("Invalid Input")

if __name__ == "__main__": 
	main()