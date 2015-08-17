import sys
from datetime import datetime
import json
from models import Message
import pytz

# convert a tweet in JSON format to a dictionary
def json2message(tweet):
    try:
        id_str = tweet["id_str"]

        # tweet text (escape double quotes, remove newlines and tabs)
        text = tweet["text"]
        text = text.replace("\"","\\\"").replace("\n","")
        text = text.replace("\t"," ")

        # user
        username = tweet["user"]["screen_name"]

        # geolocation
        if tweet['coordinates']:
            coordinates = tweet['coordinates']['coordinates']
        else:
            coordinates = None

        language = tweet['lang']

        # timestamp
        created_at = datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y") #  Wed Feb 08 22:49:40 +0000 2012
        timestamp = datetime.strftime(created_at, "%s")

        # write record in CSV format (if language is Italian)
        message = Message(author=username,
                          source='twitter',
                          timestamp=datetime.utcfromtimestamp(eval(timestamp)).replace(tzinfo=pytz.utc),
                          content={'id':tweet['id'], 'text':text.encode("utf-8")})

        return message

    # tweet is unreadable
    except:
        sys.stderr.write("error parsing tweet\n")
        return None

def read_tweets_from_file(json_file):
    messages = []
    for line in open(json_file):
        message = json2message(json.loads(line.rstrip()))
        if message:
            messages.append(message)
    return messages
