#!/usr/bin/python3
'''Get top 10 hot posts'''
import pprint
import requests

BASE_URL = 'http://reddit.com/r/{}/hot.json'

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query.
    """

    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(BASE_URL.format(subreddit),
                headers=headers)

    # Check for 404 status code
    if response.status_code == 404:
        print(None)
        return

    data = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not data:
        print(None)
        return

    for post in data[0:10]:
        print(post.get('data', {}).get('title'))
