import spotify_client
import requests
from urllib.parse import urlencode
import json
from configparser import ConfigParser
from termcolor import colored

song_list = []
config = ConfigParser()
config.read('config.ini')


def get_get_token_header():
	access_token = spotify_client.extract_access_token()[0]
	return {
		'Authorization': f'Bearer {access_token}'
	}


def get_user_playlist():
	while config['user']['playlist_id'] == '':
		playlist_id_new = input(
			colored('We need the Playlist ID. Please enter the ID: ', 'yellow'))

		if playlist_id_new == '':
			continue
		config['user']['playlist_id'] = playlist_id_new
		# save to a file
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
			print(colored('Playlist has been updated.', 'green'))
		continue

	playlist_id = config['user']['playlist_id']
	url = config['endpoints']['base_url']
	version = '/v1'
	action = '/playlists'
	token_headers = get_get_token_header()
	endpoint = f'{url}{version}{action}/{playlist_id}/tracks'
	r = requests.get(endpoint, headers=token_headers)

	if r.status_code in range(200, 299):
		# print(r.json())
		data_tracks = (r.json())
		totaltracks=data_tracks['total']
		for item in data_tracks['items']:
		    if item is not None:
		        track_name = item['track']['name']
		        track_artist = item['track']['artists'][0]['name']
		        song_list.append([(track_artist, track_name)])

		while data_tracks['next'] is not None:
			r = requests.get(data_tracks['next'], headers=token_headers)
			data_tracks = (r.json())

			if r.status_code in range(200, 299):
				for item in data_tracks['items']:
					if item is not None:
						track_name = item['track']['name']
						track_artist = item['track']['artists'][0]['name']
						song_list.append([(track_artist, track_name)])
		
		print((colored(
			f"Succes! We found {totaltracks} track(s). Status Code: {r.status_code}", 'green')))
		return song_list
	else:
		print("Invalid request!")
