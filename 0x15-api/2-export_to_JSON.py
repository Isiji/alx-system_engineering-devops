#!/usr/bin/python3
"""
Records all tasks that are owned by this employee.

Format:
    {
        "USER_ID": [
            {
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"
            },
            {
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"
            },
            ...
        ]
    }

File name:
    USER_ID.json

Usage:
    python3 script_name.py USER_ID

Arguments:
    USER_ID: The ID of the employee whose tasks need to be recorded.

Dependencies:
    - requests
    - json

Example:
    python3 script_name.py 2
    This will record all tasks owned by the employee with ID 2
    into a JSON file named "2.json".
"""

import json
import requests
import sys

if __name__ == "__main__":
    # The base URL of the API
    url = "https://jsonplaceholder.typicode.com/"

    # Extracting user ID from the command line arguments
    user_id = sys.argv[1]

    # Retrieving user data
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Retrieving tasks for the user
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    # Creating data to export in JSON format
    data_to_export = {user_id: []}
    for todo in todos:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        data_to_export[user_id].append(task_info)

    # Writing data to a JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
