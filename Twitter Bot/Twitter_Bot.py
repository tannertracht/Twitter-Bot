import tweepy as tp
import darksky
import time
import schedule
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




# Set up the schedule bitch
nampa = forecast(dark_sky_key, 43.5407, -116.5635)
def weatherCheck():
    nampa.refresh
    hourlyRainReport = []
    for hour in nampa.hourly[:19]:
        if (hour.precipProbability == 0):
            hourlyRainReport.append('No')
        elif (hour.precipProbability <= 40):
            hourlyRainReport.append('Probably Not')
        elif (hour.precipProbability <= 60):
            hourlyRainReport.append('Maybe')
        elif (hour.precipProbability <= 95):
            hourlyRainReport.append('Probably')
        else:
            hourlyRainReport.append('Yes')

    return hourlyRainReport
def buildTweet(report):
    if (report.count('Yes') > 0):
        return 'Yes'
    elif (report.count('Probably') > 0):
        return 'Probably'
    elif (report.count('Maybe') > 0):
        return 'Maybe'
    elif (report.count('Probably Not')):
        return 'Probably not'
    else:
        return 'No'

def dailyTweet():
    # tp.postupdate(buildTweet())
    print(buildTweet(weatherCheck()))

dailyTweet()
