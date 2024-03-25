#!/usr/bin/python3
"""
Records all tasks that are owned by this employee.

Format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

File name:
    USER_ID.csv

Usage:
    python3 script_name.py USER_ID

Arguments:
    USER_ID: The ID of the employee whose tasks need to be recorded.

Dependencies:
    - requests
    - csv

Example:
    python3 script_name.py 2
    This will record all tasks owned by the employee with ID 2 into
    a CSV file named "2.csv".
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # The base URL of the API
    url = "https://jsonplaceholder.typicode.com/"

    # Extracting user ID from the command line arguments
    user_id = sys.argv[1]

    # Getting the user details
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()

    # Getting the username
    username = user.get("username")

    # Getting the to-do list for the user
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    # Open a CSV file to write the tasks
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"),
                             todo.get("title")])
