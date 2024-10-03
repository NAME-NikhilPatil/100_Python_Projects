from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li h3#title-of-a-story")  # Use a specific class or ID for titles
song_names = [song.getText().strip() for song in song_names_spans]

print("Scraped song names:", song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="c6b6296132454d9081145f10ddc567d9",
        client_secret="eb93aa58220645e9b1951f939bee8797",
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
print("User ID:", user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    # Use a basic search query first
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(f"Search result for '{song}':", result)  # Debugging print
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print("Playlist:", playlist)

if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
else:
    print("No songs found to add to the playlist.")
