# Creating an API Key and Querying the API
import os
from googleapiclient.discovery import build

api_key = os.environ.get('YouTubeApiKey')

# connecting to the youtube service
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='contentDetails, statistics',
    id='***********'
    )
# ^ creates a request to the api
# contentDetails -> more info about specific channel

# getting a response
response = request.execute()
print(response)


