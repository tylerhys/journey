from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt",
        username="", 
    )
)
user_id = sp.current_user()["id"]

input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")
url = f"https://www.billboard.com/charts/hot-100/{input}/"
year = input.split("-")[0]

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [f"track: {song.getText().strip()} year: {year}" for song in song_names_spans]
song_uris = []

for song in song_names:
    result = sp.search(q=song, type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"Time Machine Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)