# oauth 2 will allow you or your users
# to give our scripts
# and applications limited access to
# third-party accounts

# if i wanted to
# also view my private or unlisted videos
# then i would need to give my script
# permission to view my
# youtube accounts data

import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
# we can ^ authenticate with oauth
from google.auth.transport.requests import Request

credentials = None

# token.pickle stores the user's credentials from previously successful logins
if os.path.exists('token.pickle'):
    print('Loading Credentials From File...')
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Tokens...')
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=[
                'https://www.googleapis.com/auth/youtube.readonly'
            ]
             # ^ scope of the information our script can access
             # ^ if we actually wanted to make
             # modifications to our account or
             # view different information then we would
             # need to tell our script exactly what
             # scopes our script will be accessing
        )
        # ^ loads all of our credentials

        flow.run_local_server(port=8000, prompt='consent',
                              authorization_prompt_message='')
        # ^ google is going to run a local web server for us and 
        # -open up a page for us to log into our google account
        # consent ->  give me a refresh token every time i run this even when i'm testing
        # ^ once we log in and are properly authorized then 
        # it's going to set our credentials within this flow object
        # ^ authorization_prompt_message='' <- we won't see the prompt for signing in anymore
        credentials = flow.credentials

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)


youtube = build('youtube', 'v3', credentials=credentials)
      
request = youtube.playlistItems().list(
    part='status, contentDetails ',
    playlistId='******'
)

response = request.execute()

for item in response['items']:
    vid_id = item['contentDetails']['videoId']
    yt_link = f"https://youtu.be/{vid_id}"
    print(yt_link)

