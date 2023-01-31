# spotify_player_python
 A music player that can play songs from Spotify built using Python only.

# Getting Started with Spotify API

To use the Spotify API, we need the "Client ID" and "Client Secret" that the Spotify API provides. We'll also need to add a redirect URL on which we want to land once the user grants us the required permissions.

Creating an app:

1. Go to the Spotify registration page and create your Spotify account.
2. Once  the account has been created, go to the Developers Dashboard. The Spotify Developer Terms of Service will appear. When we accept these terms, we'll be redirected to the Developers Dashboard.
3. Click the "CREATE AN APP" button. A dialog box requesting the app's name and description will pop up.
4. Fill in this information and click the "CREATE" button. We'll be redirected to the app overview page.

Fetch the "Client ID" and "Client Secret":

1. Click the "SHOW CLIENT SECRET" button to reveal the "Client Secret" key.
2. Copy the "Client ID" and "Client Secret" keys.
3. Assign the values of "Client ID" and "Client Secret" to client_id and client_secret keys respectively.

The official documentation of spotify APi is [here](https://developer.spotify.com/documentation/).

# Installation
Github:

```$ git clone https://github.com/aneeshkp246/spotify_player_python.git```
      
Python Packages:

```pip install -r requirements.txt```
      
Or just:

```pip install spotipy```

# Usage

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt ( Windows) .`

After that you can start it with

```python spotify_player_python.py```
