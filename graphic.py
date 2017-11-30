#**********************************************************
#Module to generate various kind of graphs
#**********************************************************

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import matplotlib.dates, time 

#returns the polarity of tweets in a list and the corresponding epoch time
def _getPolarityAndEpoch():
	#retrieving data from .csv again
	df=pd.read_csv("tweetpolarity.csv",header=None)
	data=df.values
	polarity=[]
	time_string=[]

	for row in data:
		polarity.append(row[1])
		time_string.append(row[2])

	#This one takes created_at value, strips it and makes it a standard unix epoch value.
	#Then the epoch value is converted into matplotlib date format so python recognizes it.
	#Once, the values are recognized, the overlapping can be avoided by auto-formatting in further code.
	unix_epoch_secs=[]
	for value in time_string:
		unix_epoch_secs.append(matplotlib.dates.epoch2num(time.mktime(time.strptime(value,"%a %b %d %H:%M:%S +0000 %Y"))))

	return polarity, unix_epoch_secs	

#function for plotting pie chart	
def pie_chart(positive,negative,neutral,i,keyword):
	labels = 'Positive','Negative','Neutral','Uncategorized'
	sizes = [positive,negative,neutral,i-(positive+negative+neutral)]
	colors=['gold','yellowgreen','lightcoral','lightskyblue']
	explode = (0, 0, 0, 0.1)  # explode 4th slice depicting uncategorized data	
	plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
	plt.axis('equal')
	plt.title('Twitter Reaction to Keyword #'+keyword,fontsize=18)
	plt.show()

#function for plotting bar chart
def bar_charts(positive,negative,neutral,i,keyword):
	objects = ('Positive','Negative','Neutral','Uncategorized')
	y_pos = np.arange(len(objects))
	performance = [positive,negative,neutral,i-(positive+negative+neutral)]
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.xlabel("Reactions",fontsize=15)
	plt.ylabel('Sentiments',fontsize=15)
	plt.title('Twitter Reaction to Keyword #'+keyword, fontsize=18)
	plt.show()

#function for plotting bar chart	
def timeChart(keyword):
	polarity, unix_epoch_secs=_getPolarityAndEpoch()
	fig, ax = plt.subplots()
	#Format Y-Axis
	plt.ylim(-2.0,2.0)
	my_yticks=[" ","Negative","Neutral","Positive"," "]
	plt.yticks(np.arange(-2.0, 2.0, 1),my_yticks)
	plt.ylabel("Tweet Reaction")
	ax.xaxis.label.set_size(15)

	#Format X-Axis
	plt.xlim(unix_epoch_secs[0],unix_epoch_secs[len(unix_epoch_secs)-1])
	date_fmt = '%d-%m-%y %H:%M:%S'
	date_formatter = matplotlib.dates.DateFormatter(date_fmt)
	ax.xaxis.set_major_formatter(date_formatter)
	plt.xlabel("Timeline")
	ax.yaxis.label.set_size(15)

	#adjusting line-width depending on data density
	dy_val=0
	if len(polarity)<1000:
		dy_val=1
	elif len(polarity)<10000:
		dy_val=0.6
	else:
		dy_val=0.1
	
	#plotted the chart
	ax.plot(unix_epoch_secs, polarity,linewidth=dy_val)

	#auto-formatting the date to avoid overlapping
	fig.autofmt_xdate()
	plt.legend()
	ax.set_title('Twitter Reaction to Keyword #'+keyword, fontsize=18)
	plt.show()
	
#function for plotting bar chart	
def multilineChart(keyword):
	polarity, unix_epoch_secs=_getPolarityAndEpoch()
	fig, ax = plt.subplots()
	positive_count=[]
	negative_count=[]
	neutral_count=[]
	pos=0
	neg=0
	ntr=0
	for item in polarity:
		if item==1:
			pos+=1
			positive_count.append(pos)
			negative_count.append(neg)
			neutral_count.append(ntr)
		if item==0:
			ntr+=1
			positive_count.append(pos)
			negative_count.append(neg)
			neutral_count.append(ntr)
		if item==-1:
			neg+=1
			positive_count.append(pos)
			negative_count.append(neg)
			neutral_count.append(ntr)

	interval=len(positive_count)//10
	#Format Y-Axis
	plt.yticks(np.arange(0, len(unix_epoch_secs)-1, interval))
	plt.ylabel("Tweet Reaction")
	ax.yaxis.label.set_size(15)

	#Format X-Axis
	plt.xlim(unix_epoch_secs[0],unix_epoch_secs[len(unix_epoch_secs)-1])
	date_fmt = '%d-%m-%y %H:%M:%S'
	date_formatter = matplotlib.dates.DateFormatter(date_fmt)
	ax.xaxis.set_major_formatter(date_formatter)
	plt.xlabel("Timeline")
	ax.xaxis.label.set_size(15)

	ax.plot(unix_epoch_secs, positive_count,linewidth=1)
	ax.plot(unix_epoch_secs, negative_count,linewidth=1)
	ax.plot(unix_epoch_secs, neutral_count,linewidth=1)
	ax.legend( ('Positive','Negative','Neutral') )
	fig.autofmt_xdate()
	ax.set_title('Twitter Reaction to Keyword #'+keyword, fontsize=20)
	plt.show()