#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
exports information about his/her TODO list progress to a CSV file.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_data.get("username"),
             item.get("completed"), item.get("title")]
         ) for item in todo_data]
