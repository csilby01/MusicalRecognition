from __future__ import print_function
import requests
from urllib.parse import urlencode
import base64
import webbrowser
import spotipy

CLIENT_ID = '05009217d148447f917b83b98137bf69'
CLIENT_SECRET = '74c94b99efdd45ebb6fa01d1423c4172'
REDIRECT_URI = 'http://localhost:8000/callback/'
USER_PLAYLISTS_URL = 'https://api.spotify.com/v1/me/playlists'
AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize?'
CODE = 'AQC_56RK0ZUzL1kNNMyp8CW6qM3F7ELH2AQ51cu5CW2gkD4p8lsFutWgAhVfjBdc_rvqfdpi2EOLgNfH4ALRz0J5Jq'


auth_headers = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": "playlist-modify-public"
}

def user_authorize_Spotipy():
    ACCESS_TOKEN = spotipy.util.prompt_for_user_token(username='',scope='playlist-modify-public playlist-modify-private user-library-read',client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)
    # print("Access Token: {}".format(ACCESS_TOKEN))
    return ACCESS_TOKEN

# def user_authorize():
#     webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
#     encoded_credentials = base64.b64encode(CLIENT_ID.encode() + b':' + CLIENT_SECRET.encode()).decode("utf-8")
#     token_headers = {
#         "Authorization": "Basic " + encoded_credentials,
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     token_data = {
#         "grant_type": "authorization_code",
#         "code": CODE,
#         "redirect_uri": REDIRECT_URI
#     }  
    # response = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
    # json_resp = response.json()
    # ACCESS_TOKEN = json_resp["access_token"]
    # # print(json_resp)
    # return ACCESS_TOKEN

def create_playlist(name, public):
    response = requests.post(USER_PLAYLISTS_URL, 
                             headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}, 
                             json = {"name": name, "public": public})
    json_resp = response.json()
    return json_resp

def add_to_playlist(songs, playlistURL):
    response = requests.post(playlistURL,
                             headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"},
                             json = {"uris": songs})
    json_resp = response.json()
    return json_resp

def read_saved_tracks():
    response = requests.get("https://api.spotify.com/v1/me/tracks",
                            headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"},
                            params = {"limit" : 50})
    json_resp = response.json()
    for song in json_resp['items']:
        for artist in song['track']['artists']:
            print(artist['href'])
            #for artist in track['artists']:
                #print("Artist: {} | Genre: {}".format(artist['name'], artist['genre']))
            print('\n')
    #print(json_resp['items'])
    return json_resp

global ACCESS_TOKEN
ACCESS_TOKEN = user_authorize_Spotipy()
#     #newPlaylist = create_playlist(name = "Silly Ahh", public=False)
#     # print("Playlist: {}".format(newPlaylist))
#     #newPlaylistURL = newPlaylist['tracks']['href']
#     sillyGoofyMood = ['spotify:track:3xZek9XkEaX130o3XN9cvd', 'spotify:track:28UMEtwyUUy5u0UWOVHwiI', 'spotify:track:02JIdsrod3BYucThfUFDUX', 'spotify:track:4Cd01GWLuMTNZhW0DE7cF4', 'spotify:track:1rKBOL9kJfX1Y4C3QaOvRH', 'spotify:track:3hSs17SMNlysCjVWkaJPFd']
#     #add_to_playlist(sillyGoofyMood, newPlaylistURL)
#     read_saved_tracks()

