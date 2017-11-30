#**************************************************************
#Function definition for connecting to Streaming API's and 
#save the tweets in a .csv file
#**************************************************************

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time, sys, config

class listener(StreamListener):
	def __init__(self,filename):
		self.filename=filename
		
	def on_data(self,data):
		try:
			print data
			saveFile=open(self.filename,'a')
			saveFile.write(data)
			saveFile.close()
			return True
		except BaseException,e:
			print 'failed ondata,',str(e)
			time.sleep(5)
		
	def on_error(self,status):
		print status
		
def fetchTweets(keyword,filename):
	auth=OAuthHandler(config.ckey,config.csecret)
	auth.set_access_token(config.atoken,config.asecret)
	twitterStream=Stream(auth,listener(filename))
	twitterStream.filter(track=[keyword])
