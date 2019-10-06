import tweepy
import random
import time

from datetime import datetime, timedelta

print('why i am so wise')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

kawaiiFaces = [' ↁ_ↁ', ' (ಠ_ರ)', ' (-＿- )ノ', ' щ(ಥДಥщ)', ' (￣□￣)', ' ☉▵☉凸', ' ┬──┬ ノ( ゜-゜ノ)']
nietzscheQuotes = ["In proportion as an ideal world has been falsely assumed, reality has been robbed of its value, its meaning, and its truthfulness.", "Alternate translation: Philosophy, as I have until now understood and lived it, is the voluntary life in ice and high mountains—the seeking out of everything strange and questionable in existence, everything that up to now has been banned by morality.", "How much truth can a certain mind endure, how much truth can it dare? These questions became for me ever more and more the actual test of values."]
iChingQuotes = ["To nourish oneself on ancient virtue induces perseverance.", "An army must set forth in proper order. If the order is not good, misfortune threatens.", "The superior man falls back upon his inner worth In order to escape the difficulties. He does not permit himself to be honored with revenue."]

randomFace = random.choice(kawaiiFaces)
randomNietzsche = random.choice(nietzscheQuotes)
randomiChing = random.choice(iChingQuotes)

while 24:
    api.update_status(randomNietzsche + randomFace)

    dt = datetime.now() + timedelta(hours=24)
    dt = dt.replace(hour=6)

    while datetime.now() < dt:
        time.sleep(24)

while 24:
    api.update_status(randomiChing + randomFace)

    dt = datetime.now() + timedelta(hours=24)
    dt = dt.replace(hour=24)

    while datetime.now() < dt:
        time.sleep(24)
