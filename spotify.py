import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your own credentials
client_id = "CLIENT_ID"
client_secret = "CLIENT_SCREET"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="URL_THAT_YOU_WANT_TO_OPEN",
        scope="user-top-read",
    )
)
results_top50 = sp.current_user_top_tracks(limit=50, offset=0, time_range="long_term")
results_top50_to_100 = sp.current_user_top_tracks(
    limit=50, offset=50, time_range="long_term"
)


top_songs = []
for item in results_top50["items"]:
    # Add more items as needed
    title = item["name"]
    artist = item["artists"][0]["name"]
    image = item["album"]["images"][0]["url"]
    link = item["external_urls"]["spotify"]
    top_songs.append({"title": title, "artist": artist, "image": image, "link": link})

for item in results_top50_to_100["items"]:
    # Add more items as needed
    title = item["name"]
    artist = item["artists"][0]["name"]
    image = item["album"]["images"][0]["url"]
    link = item["external_urls"]["spotify"]
    top_songs.append({"title": title, "artist": artist, "image": image, "link": link})


with open("top_songs.json", "w") as f:
    json.dump(top_songs, f, indent=4)

print("Top songs saved to 'top_songs.json'")
