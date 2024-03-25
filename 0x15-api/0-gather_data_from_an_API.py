#!/usr/bin/python3
#this script gets data of  an emloyee through an API
#display on the standard output the employee TODO list
#progress in this exact format:
#First line: Employee EMPLOYEE_NAME is done with tasks
#(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
#EMPLOYEE_NAME: name of the employee
#NUMBER_OF_DONE_TASKS: number of completed tasks
#TOTAL_NUMBER_OF_TASKS: total number of tasks,
#which is the sum of completed and non-completed tasks
#Second and N next lines display the title of completed tasks:
#TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE

import requests
import sys


if __name__ == "__main__":
    #we start by inputing the url of the API
    The_API = "https://jsonplaceholder.typicode.com/"

    #we extract the employee id from the command line
    employee_id = sys.argv[1]
    #retrive user data
    user_response = requests.get(The_API + "user/{}".format(employee_id))
    user = user_response.json()
    username = user.get("username")
    #retrieve todo list for a specific employee
    params = {"userId": employee_id}
    todos_response = requests.get(The_API + "todos", params=params)
    todos = todos_response.json()
    #create a list of completed work
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    #output progress
    print("Employee {} is done with tasks{}/{}".format(username,
        len(completed),len(todos)))
    #output completed tasks
    for complete in completed:
        print(f"\t {complete}")
