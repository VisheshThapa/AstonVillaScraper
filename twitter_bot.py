import tweepy
from datetime import datetime
import scraper
import time
print('this is my twitter bot')

CONSUMER_KEY = 'ClI0LoCCPeVTbV3cFkZPNo6yj'
CONSUMER_SECRET = 'iaODMvPndVFR2ZzBGTnC6UEZLz2j8tjMVWxAvDumAymVW3JN4x'
ACCESS_KEY = '1278799397212413952-BtrEgjVr3A1WpWmxuY2z16mS5wUZRw'
ACCESS_SECRET = 'FNnkLmpgTq1xQ5I05Qbr6aciqLtTIWhHwZ6DlGxOSa39C'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()

mentions = api.mentions_timeline()

tweet_mentions = api.mentions_timeline()

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
def reply():
    tweet_mentions = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweet_mentions):
        print(str(tweet.id) + ' -- ' + tweet.full_text)
        if '@DidAston' in tweet.full_text:
            api.update_status("@" + tweet.user.screen_name +  " " + scraper.replay_last_game(), tweet.id)
            api.create_favorite(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

def post():
    api.update_status(scraper.check_if_win())
    scraper.store_aston_track(scraper.aston_file ,scraper.aston_wins, scraper.aston_draws, scraper.aston_loss)


while True:
    if(str(scraper.next_match_date) == str(scraper.today_date)):
        if(str(scraper.next_match_time) == str(scraper.today_time)):
            time.sleep(6600)
            post()
    reply()
    time.sleep(10*60)




