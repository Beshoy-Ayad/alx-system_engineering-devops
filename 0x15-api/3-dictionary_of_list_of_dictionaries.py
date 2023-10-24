#!/usr/bin/python3
"""
Python script that, using this REST API, exports information about all
employees' TODO list progress to a JSON file.
"""

import json
import requests


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    json_data = {}
    for user in user_data:
        user_id = str(user['id'])
        json_data[user_id] = [
            {
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            for task in todo_data
            if task['userId'] == user['id']
        ]

    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)
