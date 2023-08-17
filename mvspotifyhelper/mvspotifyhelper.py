import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

import requests
import pandas as pd
import numpy as np
import json
import os
import dotenv
import sys
sys.tracebacklimit = 0 # turn off the error tracebacks

from colorthief import ColorThief
from urllib.request import urlopen
import io

dotenv.load_dotenv()


username = 'michael_vaden'

spot_id = os.getenv('spot_id')
spot_secret = os.getenv('spot_secret')
redirect_uri= 'https://www.virginia.edu/'


client_credentials_manager = SpotifyClientCredentials(client_id=spot_id, client_secret=spot_secret)


scope = "playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-library-modify"

token = util.prompt_for_user_token(username, scope, spot_id, spot_secret, redirect_uri, show_dialog=True)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth=token)

class MV():
    def get_tracks(user, playlist):
        myjson = sp.user_playlist_tracks(user, playlist)

        tracks = myjson['items']

        while myjson['next']:
            myjson = sp.next(myjson)
            tracks.extend(myjson['items'])

        return pd.json_normalize(tracks)

    def get_tracks_from_url(username, url):
        playlist_URI = url.split("/")[-1].split("?")[0]

        return MV.get_tracks(username, playlist_URI)

    def add_song_features(df):
        song_features = pd.DataFrame()
        for track in df['track.uri']:
            song_features = pd.concat([song_features, pd.json_normalize(sp.audio_features(track))])

        return df.merge(song_features, left_on='track.uri', right_on='uri')

    def get_dominant_RGB(url):
        fd = urlopen(url)
        img= io.BytesIO(fd.read())
        c1 = ColorThief(img)
        return c1.get_color(quality=1)