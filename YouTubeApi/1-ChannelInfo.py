# Creating an API Key and Querying the API
import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

api_key = os.environ.get('YouTubeApiKey')

# connecting to the youtube service
youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlists().list(
    part='contentDetails, snippet',
    channelId='UCCezIgC97PvUuR4_gbFUs5g'
    )
# ^ creates a request to the api
# contentDetails -> more info about specific channel

# getting a response
pl_response = pl_request.execute()
# ^ 1st 5 playlists in the channel

for item in pl_response['items']:
    print(item)
    print()

