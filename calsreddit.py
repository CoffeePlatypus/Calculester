import praw , random
from env import Env

class CalsReddit:
    
    def __init__(self, ENV : Env):
        self.reddit = praw.Reddit(client_id= ENV.REDDIT_CLIENT_ID,
                            client_secret=ENV.REDDIT_SECRET,
                            user_agent='Calculester',
                            username='coffeeplatypus',
                            password=ENV.REDDIT_PASS)
    
    def getRandomRedditPost(self, subname):
        return self.reddit.subreddit(subname).random().url
