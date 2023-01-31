import requests
import webbrowser
import spotipy

client_id = 'your_spotify_client_id'
client_secret = 'your_spotify_client_secret'

# auth_header = {
#   'Authorization': 'Basic ' + (client_id + ':' + client_secret)
# }
#
# auth_response = requests.post('https://accounts.spotify.com/api/token', headers=auth_header, data={
#   'grant_type': 'client_credentials'
# })
# print(auth_response.text)
# access_token = auth_response.json()['access_token']

SPOTIFY_TOKEN = "https://accounts.spotify.com/api/token"
request_body = {
    "grant_type": "client_credentials",
    "code": "code",
    "redirect_uri": 'http://localhost:8888/callback',
    "client_id": client_id,
    "client_secret": client_secret,
}
r = requests.post(url=SPOTIFY_TOKEN, data=request_body)
resp = r.json()['access_token']

spotify = spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#  redirect_uri='http://localhost:8888/callback',
#  token=access_token

# Create a Spotify client
client = spotipy.Spotify(auth=resp)


def play():
    # Extract the first result from the search results
    track = results['tracks']['items'][0]
    print(track)

    # Get the URI of the track
    track_uri = track['uri']
    print(track_uri)

    # Start playing the track
    webbrowser.open(track_uri)


def art():
    # Extract the first result from the search results
    track = results['artists']['items'][0]
    # print(track)

    # Get the URI of the track
    track_uri = track['uri']

    # Start playing the track
    webbrowser.open(track_uri)


def alb():
    # Get the first album in the list of results
    album = results["albums"]["items"][0]
    print(album)

    album_uri = album['uri']
    print(album_uri)

    webbrowser.open(album_uri)


# Search for a song
print("Welcome to Spotify! Here you can play about 82 million songs from over 11 million various artists. You just need"
      " to enter the \nsong's name and the artist's name to play the song.\n")
while True:
    print("Type: \n1. To enter a song you want to play\n2. To enter a song you want to play of a particular artist\n"
          "3. To play top tracks of an artist\n4. To exit Spotify player")
    choice = int(input())
    if choice == 1:
        print("Enter the name of the song you want to play")
        track_name = input()
        results = client.search(q='track:%s' % track_name, type='track')
        print(results)
        play()
    elif choice == 2:
        print("Enter the name of the song you want to play")
        track_name = input()
        print("Enter the artist's name")
        artist_name = input()
        results = client.search(q='track:%s artist:%s' % (track_name, artist_name), type='track')
        # print(results)
        play()
    elif choice == 3:
        print("Enter the name of the artist whose top tracks you want to play")
        artist_name = input()
        results = client.search(q='artist:%s' % artist_name, type='artist')
        # print(results)
        art()
    elif choice == 4:
        print("Thank you for playing Spotify!")
        break
    else:
        print("Invalid Input! Try again.")
