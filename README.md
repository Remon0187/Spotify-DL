# Spotify-DL
Find all tracks in a given playlist and download each track from YouTube.

## Required modules 🧾
`pip install -r requirements.txt`

## Configuration ✔️
1. Install required modules: `pip install -r requirements.txt`
1. Sign up at https://developer.spotify.com/dashboard/, create an app.
2. Enter your client id and secret in `config.ini`
3. Get the Playlist ID from the playlist you would like to download:
	* Select Spotify playlist -> Share -> Copy link to playlist
4. Copy the section between playlist/ and ?s= and add to the `config.ini` playlist_id
	* Example: `7hRA3QjxMhHd0YnD0VvExf`

## Usage 📘

- #### To download a playlist, run

  ```bash
  python spotify_downlodad.py [playlistID]
  ```
The default playlist download location is C:\Users\<username>\Documents\GitHub\Spotify-DL\Downloads

![Example](https://github.com/remonhob/Spotify-DL/blob/master/example.png)
	
# To-Do 💡
1. Integrate ZippyShare & 1Gabba
2. Custom search for direct download
3. Merge YT playlist with Spotify playlist for back-up
4. Multiple Playlist ID's
