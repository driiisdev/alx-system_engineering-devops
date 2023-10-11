#!/usr/bin/python3
'''Get top 10 hot posts'''
import pprint
import requests

BASE_URL = 'http://reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    '''Get top 10 hot posts'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(BASE_URL.format(subreddit),
                            headers=headers)

    # Check for 404 status code
    if response.status_code == 404:
        print("Subreddit does not exist")
    return

    data = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not data:
        return print("None")
    for post in data[0:10]:
        print(post.get('data', {}).get('title'))
