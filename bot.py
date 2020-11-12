import tweepy
import time

CONSUMER_KEY='rY20sBGiMATMJg90tOZj9eh8f'
CONSUMER_SECRET='axteW5xy0oCZnL8hUKbEYlPNqbGwUpiP2SyLfuZAnGpylnO7xL'
ACCESS_KEY='2532730778-30xozdq7FBrzSpja0RGUdUiA49reFmvZ3T7Mv8k'
ACCESS_SECRET='uv18OCjklAXIeeBBmoMPAQL8RlJniSqC3ppsnGTL1RbLz'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api=tweepy.API(auth)
mentions=api.mentions_timeline()

for mentions in mentions:
    print(str(mentions.id)+'-'+mentions.text)
    if '#if' in mentions.text.lower():
        print('Found GOD WORD')
        print('responding')
        
file_name='last_seen_id.txt'
def retrive_last_seen_id(file_name):
    f_read=open(file_name,'r')
    last_seen_id=int(f_read.read().strip())
    f_read.close()
    return last_seen_id
def store_last_seen_id(last_seen_id,file_name):
    f_write=open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('Retriving and Replying to tweets',flush=True)
    last_seen_id=retrive_last_seen_id(file_name)
    mentions=api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id)+'-'+mention.text,flush=True)
        last_seen_id=mention.id
        store_last_seen_id(last_seen_id,file_name)
        if '#if' in mentions.text.lower():
            print('found #if ',flush=True)
            print('responding back ',flush=True)
            api.update_status('@'+mention.user.screen_name+'#Hello world back to you',mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
    
# t0=mentions[0]0
# t0.text.lower()
