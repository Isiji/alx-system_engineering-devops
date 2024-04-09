#!/bin/usr/python3
"""
Module that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    response = response.json().get('data')
    after = response.get('after')
    children = response.get('children')

    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list