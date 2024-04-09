#!/bin/usr/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Queries the Reddit API and returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    try:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            title = child.get('data').get('title').lower().split()
            for word in word_list:
                if word.lower() in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        if len(word_count) == 0:
            return None
        for key in sorted(word_count.keys()):
            print("{}: {}".format(key, word_count[key]))
    except Exception:
        pass