import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
pp = pprint.PrettyPrinter()
CLIENT_ID = "YOUR OWN"
CLIENT_SECRET = "YOUR OWN"
REDIRECT_URL = "http://localhost:8000"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL))

def retrieve_access_token():

    access_token = sp.auth_manager.get_access_token()["access_token"]
    return access_token
def get_recommendations():
    songs = sp.recommendations(seed_genres=["rock, pop"], limit=100)["tracks"]
    for idx, song in enumerate(songs):
        print(f"{idx + 1}.")
        print("Name: ", song["name"])
        print("Artist: ", song["artist"])

def get_artist_recommendations(artist_name, genres):
    response = sp.search(q=artist_name, type="artist")["artists"]
    artist_uri = response["items"][0]["uri"]

    artist_songs = sp.recommendations(seed_artists=[artist_uri], seed_genres=[genres], limit=5)["tracks"]
    print("We recommended a few songs based on the artist you provided. ")
    print('\n')
    for idx, artist_song in enumerate(artist_songs):
        print(artist_songs[idx]["name"])

    

get_artist_recommendations("Taylor Swift", "pop")
