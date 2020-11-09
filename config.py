## Program that assigns key authoritzation variables

import os
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Define username for token
username = input("Enter Spotify Username: ") # This must be the username registered under the Spotify 
                                            #     for Developers account for this app

# Assign environemnt variables 
client_id = # Put your Spotify for Developers Web App Client ID Here
client_secret = # Put your Spotify for Developers Web App Client Secret Here
redirect_uri = # Put your Spotify for Developers Web App Redirect URI Here

# Define an authorization scope given the specific query 
scope = 'playlist-modify-private user-top-read user-library-read user-follow-read'

# Authentication
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Create an authorization token 
token = util.prompt_for_user_token(username=username, scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
