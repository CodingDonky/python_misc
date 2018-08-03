# First Reddit Bot

import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "My first python bot v0.1")
    return r

def run_bot(r):
    subreddit = r.subreddit('dbz')
    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")

r = bot_login()
run_bot(r)
