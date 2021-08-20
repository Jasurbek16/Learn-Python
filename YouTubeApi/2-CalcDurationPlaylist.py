import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

######################################################################
# Calculating a total duration of a playlist specified by an id
######################################################################

api_key = os.environ.get('YouTubeApiKey')

youtube = build('youtube', 'v3', developerKey=api_key)

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')
# ^ would find those

total_seconds = 0

# infinte loop for grabbing pages till there are none
nextPageToken = None
while True:
    
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU',
        maxResults=50,
        pageToken=nextPageToken
        )

    pl_response = pl_request.execute()


    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    # a single query to the videosResource for grabbing the videos with using the api
    vid_request = youtube.videos().list(
        part='contentDetails',
        id=','.join(vid_ids) # <- we can pass multiple using a , to separate them but the limit for ids is 50
            # ^ takes all of the items in the list and separate them with a , 
    )

    # getting info about each video duration and parsing them using reg-exes

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)
        # ^ we capture just the digits in a specific group 
        # so we can parse them out 

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0
        # get just the 1st match's number and check whether that's None or not

        video_seconds = timedelta(
                hours=hours,
                minutes=minutes,
                seconds=seconds
            ).total_seconds()

        total_seconds += video_seconds

    nextPageToken = pl_response.get('nextPageToken')
    
    if not nextPageToken:
        break

total_seconds = int(total_seconds)

minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)
print(f"{hours}:{minutes}:{seconds}")
# ^ returns a tuple of the quotient and remainder

#  Page Tokens - allow us to get 
#  all of the results one page at a time 
#  now each page is returned gives us a 
#  reference to the next page and we can 
#  keep track of which page we're on using that page token so