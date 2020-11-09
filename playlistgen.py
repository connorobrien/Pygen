### Program with a function that creates a Spotify playlist with given track ids's and playlist name

import config
import os
import random
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import sys


# Grab auth info from config.py
username = config.username
sp = config.sp
token = config.token

# Playlist creation function
def createPlaylist(lst, playlist_name):
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        # Create playlist
        playlists = sp.user_playlist_create(username, playlist_name, public=False)
        # Add tracks to playlist
        results = sp.user_playlist_add_tracks(username, playlists['id'], lst)       
    else:
        print("Can't get token for", username)
