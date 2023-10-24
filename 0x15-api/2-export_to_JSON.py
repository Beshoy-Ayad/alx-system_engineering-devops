#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
exports information about his/her TODO list progress to a JSON file.
"""

import json
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

    json_data = {
        user_id: [
            {
                'task': task['title'],
                'completed': task['completed'],
                'username': user_data['username']
            }
            for task in todo_data
        ]
    }

    json_filename = '{}.json'.format(user_id)
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)
