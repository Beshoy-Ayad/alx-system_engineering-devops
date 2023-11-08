#!/usr/bin/python3
"""
Python script that, using this REST API, for a given subreddit,
returns all its hot posts for a given subreddit.
"""

import requests

def count_words(subreddit, word_list, after=None, results=None):
    if results is None:
        results = {}

    headers = {'User-Agent': 'Mozilla/5.0'}  # Provide a user agent to prevent issues with Reddit API

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after or ""}'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: Unable to fetch data from Reddit. Status code: {response.status_code}")
        return

    data = response.json().get('data', {})
    articles = data.get('children', [])

    for article in articles:
        title = article['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                results[word] = results.get(word, 0) + title.count(word.lower())

    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, results)
    else:
        print_results(results)

def print_results(results):
    sorted_results = sorted(results.items(), key=lambda item: (-item[1], item[0].lower()))
    for word, count in sorted_results:
        print(f"{word}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Example: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)

