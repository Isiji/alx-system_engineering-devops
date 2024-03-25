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
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()

    # Check if user ID retrieved from API matches provided user ID
    if str(user_data['id']) != str(user_id):
        print("Incorrect USER_ID: Expected {}, Got {}".format(user_id,
                                                    user_data['id']))
        sys.exit(1)

    # Retrieving tasks for the user
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    # Creating data to export in JSON format
    data_to_export = {user_id: []}
    for todo in todos:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_data.get("username")
        }
        data_to_export[user_id].append(task_info)

    # Check if USER_ID's value type is a list of dicts
    if not isinstance(data_to_export[user_id],
                      list) or not all(isinstance(task, dict)
                                                    for task in data_to_export[user_id]):
            print("USER_ID's value type is not a list of dicts")
            sys.exit(1)

    # Check if all tasks found in list of dicts
    if len(todos) != len(data_to_export[user_id]):
        print("All tasks not found")
        sys.exit(1)

    # Writing data to a JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
    