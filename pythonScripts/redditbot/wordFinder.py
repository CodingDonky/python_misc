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
    word = "Rick"
    word2 = "Morty"
    word_users = set()   # to avoid duplicates
    word_users2 = set()
    for comment in r.subreddit('rickandmorty').comments(limit=250):
        if word in comment.body:
            word_users.add(comment.author)
        if word2 in comment.body:
            word_users2.add(comment.author)
    print "The users that mentioned "+ word +" are :"
    for user in word_users:
        print "  " + str(user)
    print "The users that mentioned "+ word2 +" are :"
    for user in word_users2:
        print "  " + str(user)
    print str(len(word_users)) + " users mentioned "+ word
    print str(len(word_users2)) + " users mentioned "+ word2

r = bot_login()
run_bot(r)
