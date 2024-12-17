from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import spotipy
import pandas as pd
import random
import math
#client_id="c67da3b55cb84db8a999069f1fcff3bb"
#client_secret="38c93b7d6fdd499691d6c25579e5027a"
#client_id="12308f6c7b9c4194a6ca9e06f43d3bfd"
#client_secret="e27a673a043147df8bf4a5d0a9fe8084"
#client_id = "9c1894e9a4dd49c0a52132423c1bb3fc"
#client_secret = "e7bafb5be06a450ca1909e4a64213074"
client_id="b5f10961709549ccb502d93f58921a5f"
client_secret="af7cae4ad8824baea09f20b44433510e"
#client_id = "dec967d105634e55942f249a600780f1"
#client_secret = "33524391083f4259a50bb489370a48a6"
#client_id = "a60e17678866408db8352a44845772c8"
#client_secret = "0a63db9962ed4256a574bf7ae069bf51"
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
df=pd.read_csv("kori.csv")
df=df.reset_index(drop=True)
#sub=df[450:500]
sub=df
#del sub["count"]
def get_track_album_id(id):
    metadata = sp.track(id)
    return metadata['album']['id']
def get_artist_id(id):
    metadata = sp.track(id)
    return metadata['album']['artists'][0]['id']
    
track_ids = sub['track_id'].tolist()
album_ids = [] 
for track_id in track_ids:
    album_ids.append(get_track_album_id(track_id))
    print(track_id)
artist_ids = []
for track_id in track_ids:
    artist_ids.append(get_artist_id(track_id))

sub['album_id'] = album_ids
sub['artist_id'] = artist_ids
sub.to_csv('kori_ids.csv', index=False)
