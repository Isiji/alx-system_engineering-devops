#!/usr/bin/python3
#Records all tasks that are owned by this employee
#Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
#File name must be: USER_ID.csv

import requests
import sys
import csv

if __name__ == "__main__":
    #can not be executed if imported
    url = "https://jsonplaceholder.typicode.com/"
    #exctracting user id from the command line arguments
    user_id = sys.argv[1]
    #getting the user response details
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    #getting the username
    username = user.get("username")
    #getting the to do list
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    #open a csv file
    with open("[].csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username,todo.get("completed"),
                             todo.get("title")])
