#Used for Authentication
import requests
import base64
import datetime
from configparser import ConfigParser

#Initial config 
config = ConfigParser()
config.read('config.ini')

def get_client_credentials():
    #Import from config
    client_id = config['auth']['client_id']
    client_secret = config['auth']['client_secret']
    
    #Convert to Base64
    client_creds = f'{client_id}:{client_secret}'
    client_creds_64 = base64.b64encode(client_creds.encode())
    return client_creds_64.decode()
    
def get_token_header():
    client_creds_64 = get_client_credentials()
    return {
        'Authorization': f'Basic {client_creds_64}'
    }

def get_token_data():
    #Token lookup variables
    return {
        'grant_type': 'client_credentials'
    }
    
def extract_access_token():
    token_url = config['endpoints']['token_url']
    token_data = get_token_data()
    token_headers = get_token_header()
    r = requests.post(token_url, data=token_data, headers=token_headers)
    
    if r.status_code in range(200, 299):
        now = datetime.datetime.now()
        data = r.json()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        access_data = (access_token,expires)
        return access_data
    else:
        raise Exception('The request is not valid.')