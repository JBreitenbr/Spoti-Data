from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import spotipy
import pandas as pd
import random
import math
client_id="4884e2b08e974c8b946faa2de9a92060"
client_secret="bd609f75f723401389b3524db519793f"
#client_id="12308f6c7b9c4194a6ca9e06f43d3bfd"
#client_secret="e27a673a043147df8bf4a5d0a9fe8084"
#client_id="b5f10961709549ccb502d93f58921a5f"
#client_secret="af7cae4ad8824baea09f20b44433510e"
#client_id = "dec967d105634e55942f249a600780f1"
#client_secret = "33524391083f4259a50bb489370a48a6"
#client_id = "9c1894e9a4dd49c0a52132423c1bb3fc"
#client_secret = "e7bafb5be06a450ca1909e4a64213074"
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
#df=pd.read_csv("daten.csv")
#df=df.reset_index(drop=True)
#sub=df[450:500]
sub=pd.read_csv("test_ids_5.csv").reset_index(drop=True)[["album_id"]]
sub.drop_duplicates(inplace=True)
sub=sub[200:len(sub)]
print(len(sub))
def to_min_sec(milliseconds):
    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(minutes) + ":" + str(seconds)
def get_album_name(id):
    metadata = sp.album(id)
    return metadata['name']
def get_album_pic(id):
    metadata = sp.album(id)
    return metadata['images'][1]['url']
def get_album_type(id):
    metadata = sp.album(id)
    ch=metadata['album_type']
    return ch[0].upper() + ch[1:]
def get_album_date(id):
    metadata = sp.album(id)
    return metadata['release_date']
def get_album_tracks(id):
    tracks = sp.album_tracks(id)
    stri=""
    for el in range(len(tracks['items'])):
        stri+=tracks["items"][el]['name']+" ("+to_min_sec(tracks["items"][el]['duration_ms'])+")/"
    return stri[:-1]
album_ids = sub['album_id'].tolist()
print(to_min_sec(10000))
print(get_album_tracks(album_ids[0]))
print(get_album_name(album_ids[0]))
print(get_album_type(album_ids[0]))

album_name = [] 
album_type = []
album_date = []
album_tracks = []
album_pic = []
for album_id in album_ids:
    album_name.append(get_album_name(album_id))
for album_id in album_ids:
    album_type.append(get_album_type(album_id))
for album_id in album_ids:
    album_date.append(get_album_date(album_id))
for album_id in album_ids:
    album_tracks.append(get_album_tracks(album_id))
for album_id in album_ids:
    album_pic.append(get_album_pic(album_id))

sub['album_name'] = album_name
sub['album_type'] = album_type
sub['album_date'] = album_date
sub['album_tracks'] = album_tracks
sub['album_pic'] = album_pic
sub.to_csv('album_info_5_2.csv', index=False)


