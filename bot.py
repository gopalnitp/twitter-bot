import  tweepy

print("my bot")


# Consumer keys and access tokens, used for OAuth
consumer_key = 'qsayjlxUCmm7nsCI6DjSNvnjx'
consumer_secret = 'F94MeKqkHRXU94RTrzy0YGyY423q7mIMmbZoxjVVFVDHha7U5U'
access_token = '1048493255611113473-hZU92hR7fqJX1NvHQPdl7WGUUdfMYA'
access_token_secret = 'yJ6CMy7EndVobvn6G1XXas0zwRv9TCAR1UpX5ONx3AEAI'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
import time
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
FILE_NAME = 'bot.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets(n):
    print('retrieving and replying to tweets...')
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        k=0
        f=0
        if '#hello' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back...')
            k=k+1
            api.update_status('@' + mention.user.screen_name +
                    '#HelloWorld back to you!', mention.id)
        if k!=0 and f==0:
        	print "updste no recent"
        

while True:
    reply_to_tweets(1)
    print "done"
    

    time.sleep(15)

