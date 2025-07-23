import datetime, os, requests
from bs4 import BeautifulSoup
import spotipy # type: ignore
from spotipy.oauth2 import SpotifyOAuth # type: ignore
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("SPOTIPY_USER")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URL = os.getenv("REDIRECT_URL")

today = datetime.datetime.today()


################# BILLBOARD TOP 100 SONGS #################

bill_board = "https://www.billboard.com/charts/hot-100/"

while True:
    date_input = input("Enter a date in YYYY-MM-DD format: ")
    try:
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        if date > datetime.date.today() - datetime.timedelta(days= today.weekday() + 2) or date < datetime.date(1900, 1, 1):
            print("Please enter a valid date between last week and 1900-01-01.")
            continue
        break
    except ValueError:
        print("Invalid date format. Please try again.")


date_str = date.strftime("%Y-%m-%d")
bill = f"{bill_board}{date_str}/"

try:
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
    response = requests.get(bill, headers=header)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    song_names_spans = soup.select("li ul li h3")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Billboard: {e}")
    exit()

song_names = [song.getText().strip() for song in song_names_spans]


################## SPOTIFY AUTHENTICATION #################

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="playlist-modify-private",
                                               cache_path="token.txt",
                                               show_dialog=True,
                                               username=USER))

user_id = sp.current_user()["id"]
# user name
print(sp.current_user()["display_name"])

song_uris = []
year = date_str.split("-")[0]
print(f"Searching....")

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        # song name:
        # print(result["tracks"]["items"][0]["name"])
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


print("Creating playlist...")
playlist = sp.user_playlist_create(user=user_id, name=f"{date_str} Billboard 100", public=False)

print("Adding songs to the playlist...")
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)

print("Playlist created successfully!")