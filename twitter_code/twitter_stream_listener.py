import tweepy
import json

# Consumer keys and access tokens, used for OAuth
consumer_key = 'JASIwzT3g0EXnhEAHy4rAcDdy'
consumer_secret = 'xPETNxjfb28j4wxnjfa8M8pkC2WeH4D3ntnupyy840rjGRxDx7'

access_token = '732845932816019456-ghlq703h5JmU8bSLkpfnvIFkQMijyZE'
access_token_secret = 'qKnAgh5FSYJtOeeN2dKLP5bXi3PuqikvjG509ZQtNmOQA'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    l = StdOutListener()
    print "Showing all new tweets for #coventry:"
    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['coventry'])
