import os
from googleapiclient.discovery import build

######################################################################
# Getting the most popular video in a playlist
######################################################################

api_key = os.environ.get('YouTubeApiKey')

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = '********'

videos = []

# infinte loop for grabbing pages till there are none
nextPageToken = None
while True:
    
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
        )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    # a single query to the video Resource for grabbing the videos with using the api
    vid_request = youtube.videos().list(
        part='statistics',
        id=','.join(vid_ids) # <- we can pass multiple using a , to separate them but the limit for ids is 50
            # ^ takes all of the items in the list and separate them with a , 
    )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        vid_views = item['statistics']['viewCount']

        vid_id = item['id']
        yt_link = f'https://youtu.be/{vid_id}'

        videos.append(
            {
                'views':int(vid_views),
                'url':yt_link,
            }
        )

    nextPageToken = pl_response.get('nextPageToken')
    
    if not nextPageToken:
        break

videos.sort(key=lambda vid: vid['views'], reverse=True) 

for video in videos[:10]:
    print(video['url'], video['views'])


#  Page Tokens - allow us to get 
#  all of the results one page at a time 
#  now each page is returned gives us a 
#  reference to the next page and we can 
#  keep track of which page we're on using that page token so