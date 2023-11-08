#!/usr/bin/python3
"""
Python script that, using this REST API, for a given subreddit,
returns all its hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of all hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
