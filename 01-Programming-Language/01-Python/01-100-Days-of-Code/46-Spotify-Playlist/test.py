import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="28fde953132441b8b6778a8962fa5c29",
        client_secret="465b58e725b843d4bdc339f4816e254e",
        show_dialog=True,
        cache_path="token.txt",
        username="Tyler", 
    )
)
user_id = sp.current_user()["id"]