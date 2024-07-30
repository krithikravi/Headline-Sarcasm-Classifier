import praw
import pandas as pd

secret='UAd5dM0UII9yDNbORHAjGwSxMhU1oA'
token='WVazkxdLfpMq4ak7ceJe5Q'
user_agent="Scraper by u/krflame4"
reddit=praw.Reddit(client_id=token, client_secret=secret, user_agent=user_agent, password='quickplay', username='krflame4')
headlines={}
for submission in reddit.subreddit('TheOnion').hot(limit=None):
    headlines[submission.title]=1
n=len(headlines)
for submission in reddit.subreddit('news').hot(limit=n):
    headlines[submission.title]=0
df=pd.DataFrame(headlines.items(), columns=['Headline', 'Sarcastic'])
df.to_excel('headlines.xlsx',header=False, index=False)


