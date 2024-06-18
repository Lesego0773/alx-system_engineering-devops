#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    userId = sys.argv[1]
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    if user_response.status_code != 200:
        print("User with ID {} not found".format(userId))
        sys.exit(1)
    
    user = user_response.json()
    name = user.get('name')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    if todos_response.status_code != 200:
        print("Failed to fetch TODOs")
        sys.exit(1)
    
    todos = todos_response.json()
    totalTasks = 0
    completed = 0

    for task in todos:
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks ({}/{}):'
          .format(name, completed, totalTasks))

    for task in todos:
        if task.get('userId') == int(userId) and task.get('completed'):
            print('\t {}'.format(task.get('title')))

