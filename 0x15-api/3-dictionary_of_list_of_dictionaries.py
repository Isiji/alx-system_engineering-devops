#!/usr/bin/python3
import json
import requests
from sys import argv


def export_to_json():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    all_tasks = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        response = requests.get(url)
        tasks = response.json()
        task_list = []
        for task in tasks:
            task_list.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
        all_tasks[user_id] = task_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == '__main__':
    export_to_json()
