#!/usr/bin/python
"""
Photograbber
============
Add your client ID for the Unsplash API directly in this script or as an
environment variable as UNSPLASH_CLIENT_ID. Then simply run this script with
an argument for what you are looking for. It will download the first
available image to the current working directory.

Written by Stephen Adams
"""
import requests
import sys
import os

if os.environ.get('UNSPLASH_CLIENT_ID'):
    client_id = os.environ.get('UNSPLASH_CLIENT_ID')
else:
    client_id = 'client_id_here'
url = 'https://api.unsplash.com/search/photos/?client_id=' + client_id


def get_photos(term):
    r = requests.get(url + '&query=' + term)
    print(r.json())
    data = r.json()['results'][0]['urls']['raw']
    r = requests.get(data)
    if r.status_code == 200:
        with open(os.getcwd() + '/' + term + '.jpg', 'wb') as f:
            f.write(r.content)
        f.close()
    else:
        print('url is bad')


get_photos(sys.argv[1])
