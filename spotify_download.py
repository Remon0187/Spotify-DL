import youtube_dl
import spotify_search
from youtube_search import YoutubeSearch
import json


def get_spotify_playlist():
    track_list = spotify_search.get_user_playlist()

    for track in track_list:

        for artist, name in track:

            artistname = (f'{artist} {name}')
            video_id = get_video_id(wanted_item=artistname)
            download_playlist(id=video_id)


def get_video_id(wanted_item):
    search_query = wanted_item
    results = YoutubeSearch(f'{search_query}', max_results=10).to_json()
    json_data = json.loads(results)

    for track in json_data['videos']:

        track_id = track['id']
    return track_id

"""
Prefer best quality, mp3 codec, extract mp3 with ffmpeg located in ./bin path, exctract to ./downloads folder
"""
def download_playlist(id):
    search_id = id
    ydl_opts = {
        'format': 'bestaudio/best',
            'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
         }],
        'ffmpeg_location': './bin/ffmpeg.exe',
        'outtmpl': './Downloads/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={search_id}'])

if __name__ == "__main__":
    get_spotify_playlist()
