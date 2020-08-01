import youtube_dl
import spotify_search
from youtube_search import YoutubeSearch
import json
from termcolor import colored


def get_spotify_playlist():
    track_list = spotify_search.get_user_playlist()

    for track in track_list:

        for artist, name in track:

            artistname = (f'{artist} {name} extended mix')
            video_id = get_video_id(wanted_item=artistname)
            if video_id is not None:
                try:
                    download_playlist(id=video_id)
                except:
                    print(colored(f'video for {artistname} could not be downloaded!', 'red'))
                


def get_video_id(wanted_item):
    search_query = wanted_item
    try:
        results = YoutubeSearch(f'{search_query}', max_results=10).to_json()
        json_data = json.loads(results)
        track = json_data['videos'][0]
        return track['id']
    except:
        print(colored(f'video for {wanted_item} could not be found!', 'red'))

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
