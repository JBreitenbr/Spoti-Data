from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import spotipy
import pandas as pd
import random
import math
client_id = "3068d7f48a0440a4acac15f286185052"
client_secret = "88246ad945904b459d368f2956ac92be"
#scope = "user-library-read"
username = "31nfsp7vapk4zh24xzvw3lkavx5e"
redirect_uri = 'http://localhost:8000'
scope = 'user-read-recently-played user-library-read'

import requests
from datetime import datetime
from typing import List
import spotipy.util as util
from os import listdir
import warnings
warnings.filterwarnings("ignore")
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
df=pd.read_csv("daten.csv")
df=df.reset_index(drop=True)
sub=df[4800:5000]

def get_track_pics(id):
    metadata = sp.track(id)
    return metadata['album']['images'][2]['url']
def get_track_album(id):
    metadata = sp.track(id)
    return metadata['album']['name']
track_ids = sub['track_id'].tolist()
img_urls = []
albums = []
for track_id in track_ids:
  img_urls.append(get_track_pics(track_id))
  albums.append(get_track_album(track_id))
sub['imgUrl'] = img_urls
sub['album'] = albums
sub.to_csv('batch25.csv', index=False)
