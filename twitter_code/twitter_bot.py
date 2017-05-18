#!/usr/bin/python  # lets the computer know that this file should be run with python
import tweepy # import the tweepy module http://tweepy.readthedocs.io/en/v3.5.0/
# this might need installing: sudo pip install tweepy
# if pip isn't installed then: sudo easy_install pip
import random, time #  we can import lots of modules together on a single comma seperated line

class TwitterAPI:
    # this init function sorts out the authentication
    def __init__(self):
        consumer_key = "4MDOBG8vdmPI0TwH1QfJ2k"
        consumer_secret = "7UjfZ5HvmB8pcuEz0R2eDUExxxxxxxxxxxxxxxx"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "732845932816019456-DqdpEZaBOotqQo76Z0DAD5l1mCow"
        access_token_secret = "k6xq6xxxxxxxxxxxxxxxxxgxfBecYpeS"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

# this is the function that does the tweeting
    def tweet(self, message):
        self.api.update_status(status=message)

# below is an array of tweets that later we will randomly choose from
tweets = [
    "some #tweet",
    "other tweet",
    "some #other tweet",
    "#foo #tweet",
    "LOUD tweet",
    "#tweet #tweet"
    ] # you can just keep adding stuff to the list
      # remember to add commas and no comma after the last entry

# the below if __name__ == "__main__": basically means
# "if you are running as a normal script rather than an library"
if __name__ == "__main__":
    twitter = TwitterAPI()
    while True: # this means so long as you are running
                # then just keep looping over the below code
        tweet = random.choice(tweets)
        # randomly choose something from the tweets array
        print(tweet); # print the tweet to screen for testing
        # keep the below commented while testing -
        # dont want to spam your twitter account!
        # twitter.tweet(i)
        # this calls the tweet function from the TwitterAPI() class
        # which in this instance it has been named "twitter"
        time.sleep(10); # wait for 10 seconds
