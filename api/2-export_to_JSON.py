#!/usr/bin/python3
"""
Exports data of an employee's Todo list to a JSON file.
format: {"USER_ID": [{"task": ..., "completed": ..., "username": ...}, ...]}
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Get user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Get all tasks
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Prepare JSON Structure
    task_list = []
    for task in todos:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): task_list}

    # save to file
    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
