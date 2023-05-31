import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

# requested_date = input("Enter the date you want to move back in time to (yyyy-mm-dd): ")
requested_date = '2000-08-26'
BILLBOARD_URL = f'https://www.billboard.com/charts/hot-100/{requested_date}/'
TOP_100 = {}

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://www.example.com/",
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt")
)
user_id = sp.current_user()["id"]


# Create a dictionary with top 100 songs by given date from Billboard website.
playlist_response = requests.get(url=BILLBOARD_URL).text
soup = BeautifulSoup(playlist_response, 'html.parser')
top_rows = soup.select('ul.o-chart-results-list-row')

for row in top_rows:
    position = row.select('li.o-chart-results-list__item span')[0].getText().strip()
    author = row.select('li.o-chart-results-list__item span')[1].getText().strip()
    title = row.select('li.lrv-u-width-100p ul li h3')[0].getText().strip()
    TOP_100[f'{position}'] = {'author': author, 'title': title}


# Create playlist
new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f'{requested_date} Billboard top 100',
    public=False,
    description=f'Top 100 tracks by Billboard from {requested_date}'
)

new_playlist_id = new_playlist['id']

# Get tracks uri and make a list
tracks = []
for i in range(1, 101):
    artist = TOP_100[str(i)]['author']
    song = TOP_100[str(i)]['title']

    try:
        track = sp.search(
            q=f"track: {song} artist: {artist}",
            type='track',
            market='PL',
            limit=1
        )
        track_uri = track['tracks']['items'][0]['uri']
        tracks.append(track_uri)
    except IndexError:
        print(f"'{song}' by {artist} doesn't exist in Spotify. Skipped.")

# Add tracks to playlist
sp.playlist_add_items(playlist_id=new_playlist_id, items=tracks)
