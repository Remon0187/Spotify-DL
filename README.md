# Spotify-DL
- Download a Spotify playlist or song as an MP3 file.

## Dependencies 🧾
```
pip install -r requirements.txt
```

## Configuration ✔️
1. Install required modules: ```pip install -r requirements.txt```
1. Sign up at https://developer.spotify.com/dashboard/, create an app.
3. Enter your client id and secret in `config.ini`

## Usage 📘

- #### To find a playlist or song url


- #### To download a playlist, run

```
python spotify_download.py [playlistUrl]
```
Example:
```
python spotify_download.py https://open.spotify.com/playlist/7xlcXTGPqM2v7lEdHFXyMW?si=542cfedfa8e24ccd
```

- #### To download a song, run

```
python spotify_download.py [songUrl]
```
  
The default playlist download location is C:\Users\<Username>\Documents\GitHub\Spotify-DL\Downloads

![Example](https://github.com/remonhob/Spotify-DL/blob/master/example.png)
	
# To-Do 💡
1. Integrate ZippyShare & 1Gabba
2. Custom search for direct download
3. Merge YT playlist with Spotify playlist for back-up
4. Multiple Playlist ID's
