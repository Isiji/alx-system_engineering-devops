#!/usr/bin/python3
"""
    Fetches tasks for all users from an external API and exports the data to
    a JSON file.

    This function retrieves tasks for each user from an external API endpoint,
    organizes the tasks by user ID, and then writes the data to a JSON
    file in
    the required format specified in the task requirements.

    Args:
        None

    Returns:
        None
    """

import json
import requests
import sys

# Entry point of the script
if __name__ == '__main__':
    # API endpoint to fetch user data
    url = 'https://jsonplaceholder.typicode.com/users'
    # Fetch user data from the API
    response = requests.get(url)
    # Extract user information from the response
    users = response.json()
    # Dictionary to store all tasks
    all_tasks = {}

    # Iterate over each user
    for user in users:
        user_id = str(user['id'])  
        username = user['username'] 
        # API endpoint to fetch tasks for the current user
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        # Fetch tasks for the current user from the API
        response = requests.get(url)
        # Extract task data from the response
        tasks = response.json()
        task_list = []

        # Iterate over each task of the current user
        for task in tasks:
            # Create a dictionary representing a task
            task_list.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
        # Store the list of tasks for the current user in the dictionary
        all_tasks[user_id] = task_list

    # Write the collected tasks data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)

