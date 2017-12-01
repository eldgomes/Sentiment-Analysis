# Twitter Social Media and Text Analysis
The objective of this project is to analyse the sentiment of twitter users through their tweets to understand the reaction of the people towards an ongoing event.

## Prerequisite
python 2.7.x 

The following packages need to be installed if they do not already exist: 
- pip installer
- numpy
- pandas
- matplotlib
- tweepy
- textblob

## Execution
1. Run streamTweets.py
`python streamTweets.py`.
Enter the topic and filename(as filename.csv) when prompted.

2. Stop the script manually after collecting sufficient data.

3. Run tweetAnalysis.py
`python tweetAnalysis.py`.
Enter same topic and filename(as filename.csv) as above when prompted.

4. Choose visualization from the options.


## Working
"streamTweets.py" fetches the tweets and stores in "filename.csv" as JSON objects.
"tweetAnalysis.py" fetches the required data from "filename.csv", classifies the tweets and saves the classification in a temporary file "TweetPolarity.csv". 
The visualisation module uses data from this file to draw the various graphs. 
