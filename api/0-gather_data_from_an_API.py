#!/usr/bin/python3

"""
Module: 0-gather_data_from_an_API
This module fetches and displays information about
an employee's todo list progress
using the JSONPlaceholder API. It retrieves the
employee's name and their completed tasks
based on the provided employee ID.
Usage:
    Run the script with the employee ID as a command-line argument:
        python3 0-gather_data_from_an_API.py <employee_id>
Example:
    python3 0-gather_data_from_an_API.py 1
Functions:
    This script does not define any functions but performs
    the following operations:
    - Validates the command-line argument for employee ID.
    - Fetches employee details from the JSONPlaceholder API.
    - Fetches Todo list items for the employee.
    - Filters and displays the completed tasks.
Dependencies:
    - requests: Used for making HTTP requests to the API.
    - sys: Used for handling command-line arguments and exiting the program.
API Endpoints:
    - https://jsonplaceholder.typicode.com/users/<employee_id>:
    Retrieves employee details.
    - https://jsonplaceholder.typicode.com/todos?userId=<employee_id>:
    Retrieves Todo list items.
Error Handling:
    - Ensures the employee ID is provided and is an integer.
    - Handles cases where the employee is not found or the API request fails.
Output:
    Displays the employee's name, the number of
    completed tasks, and the titles of those tasks.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # API endpoints
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )

    # Get employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    employee_name = user_response.json().get("name")

    # Get TODOs
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), len(todos)
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
