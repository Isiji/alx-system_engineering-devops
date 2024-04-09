#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Get all hot posts from subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python:Holberton School'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    after = data.get('after')
    posts = data.get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list