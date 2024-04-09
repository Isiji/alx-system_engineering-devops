#!/bin/usr/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16-api_advanced:v1.0.0 (by /u/allelomorph)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    children = data.get("children")

    for child in children[:10]:
        print(child.get("data").get("title"))