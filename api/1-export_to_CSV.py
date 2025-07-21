
#!/usr/bin/python3

"""
Exports data of an employee's Tdo list to a CSV file.
Format: "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    # file name: <USER_ID>.csv
    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
