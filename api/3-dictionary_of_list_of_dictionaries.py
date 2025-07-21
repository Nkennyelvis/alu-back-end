#!/usr/bin/python3
"""
Exports data of all employees' Todo lists to a JSON file.
Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ...]}
"""

import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    # Fetch all users
    users_response = requests.get(users_url)
    users = users_response.json()

    # fetch all todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Build a dictionary {user_id: [tasks]}
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        # Filter tasks for this user
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]
        all_data[str(user_id)] = user_tasks

    # Save to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)
        