#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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

    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    print('Employee {} is done with tasks({}/{}):'.format(
        user_data['name'], done_tasks, total_tasks))
    for task in todo_data:
        if task['completed']:
            print('\t {}'.format(task['title']))
