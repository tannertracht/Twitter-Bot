import tweepy as tp
import darksky
import time
import os
from darksky import forecast
# Twitter Keys
consumer_key = 'ecLMpcNsT5kxLQBpz0YnRW7J8'
consumer_secret = 'yfuEZWk38zAvvIeGBgAFVpsIs8ZQZW28L3qEA6mYY2eZo6833s'
access_token = '954227830568595462-wVR1e0udn9cEaMomPAKhZPwk2Lf6QGl'
access_secret = 'gwKFdw9JLMmXxtmzNO09q1mFVh8eEblAGPy2o62uUIf6v'
# Twitter Authentication
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)
# Dark Sky Key
dark_sky_key = 'bd1b01bc32d2186a8104d35667f84e8b'

nampa = forecast(dark_sky_key, 43.5407, 116.5635)
