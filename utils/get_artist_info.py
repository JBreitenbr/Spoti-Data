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
#client_id = "a60e17678866408db8352a44845772c8"
#client_secret = "0a63db9962ed4256a574bf7ae069bf51"
#client_id = "9c1894e9a4dd49c0a52132423c1bb3fc"
#client_secret = "e7bafb5be06a450ca1909e4a64213074"
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
#df=pd.read_csv("test_ids.csv")
#df=df.reset_index(drop=True)
#sub=df[5400:5600]
sub=pd.DataFrame(pd.read_csv("kori_ids.csv")["artist_id"].reset_index(drop=True))
sub.drop_duplicates(inplace=True)
def get_genres(id):
    metadata = sp.artist(id)
    genres=metadata['genres']
    stri=""
    for el in genres:
        subel=el.split(" ")
        for s in subel:
            s=s[0].upper()+s[1:]
            if s[1:]==subel[-1][1:]:
                stri+=s+"/"
            else:
                stri+=s+" "
    return stri[:-1]

artist_ids = sub['artist_id'].tolist()
genres = []
print(get_genres(artist_ids[0]))
for artist_id in artist_ids:
  genres.append(get_genres(artist_id))
sub['genres'] = genres
sub.to_csv('kori_genres.csv', index=False)
