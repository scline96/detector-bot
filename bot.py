# install pip

# https://www.youtube.com/watch?v=krTUf7BpTc0

import praw
import config

# busterroni$ pip install praw


def bot_login():
    login = praw.Reddit(username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "test bot v0.1")
    return login

def run_bot(login):


login = bot_login()

