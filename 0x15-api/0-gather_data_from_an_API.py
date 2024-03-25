
import requests
import sys


if __name__ == "__main__":
    The_API = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_response = requests.get(The_API + f"user/{employee_id}")
    user = user_response.json()
    params = {"userId": "employee_id"}
    todos_response = requests.get(The_API + "todos", params=params)
    todos = todos_response.json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks{}/{}".format(user.get("name"),len(completed),len(todos)))

    for complete in completed:
        print(f"\t {complete}")
