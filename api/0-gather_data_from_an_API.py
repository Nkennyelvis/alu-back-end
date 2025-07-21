
#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <Employee_id>")
        sys.exit(1)

    try:
        Employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # API endpoints
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(Employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(Employee_id)
    )

    # Get employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    Employee_name = user_response.json().get("name")

    # Get TODOs
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            Employee_name, len(done_tasks), len(todos)
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
