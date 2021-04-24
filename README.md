# Spotify-Download
Find all tracks in a given playlist and download each track from YouTube.

# Required modules
* requests
* configparser
* urlencode
* termcolor
* youtube_search

# Configuration ✔️
1. Sign up here -> https://developer.spotify.com/dashboard/, create an app.
2. Enter your client id and secret in config.ini
3. Get the Playlist ID from the playlist you would like to download:
	* Select Spotify playlist -> Share -> Copy link to playlist
4. This will get you a full playlist link that looks like the following:
https://open.spotify.com/playlist/ `{playlist ID}` ?si=
The playlist id is the string right after playlist/ as marked above.
4. Example: `7hRA3QjxMhHd0YnD0VvExf`

# Usage
`python3 spotify_download.py`

![Example](https://github.com/remonhob/Spotify-DL/blob/master/example.png)
	
# To-Do 💡
1. Integrate ZippyShare & 1Gabba
2. Custom search for direct download
3. Merge YT playlist with Spotify playlist for back-up
4. Multiple Playlist ID's
