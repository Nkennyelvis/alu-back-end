
#!/usr/bin/python3

"""
This script fetches employee Todo list progress from a REST API.
It takes an an employee ID as a command-line argument and displays
the employee's name, the number of completed tasks out of the total,
and the titles of the completed tasks.
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the todo list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch user information
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        # Raise an HTTPError for bad responses (4xx or 5xx)
        user_response.raise_for_status()
        user_data = user_response.json()
        # Get employee name and strip any leading/trailing whitespace
        employee_name = user_data.get("name", "").strip()

        if not employee_name:
            print(f"Error: Employee with ID {employee_id} not found.")
            return

        # Fetch todo list for the employee
        todos_response = requests.get(f"{base_url}/todos",
                                      params={"userId": employee_id})
        # Raise an HTTPError for bad responses (4xx or 5xx)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        # Filter for completed tasks
        completed_tasks = [task for task in todos_data
                           if task.get("completed") is True]
        number_of_done_tasks = len(completed_tasks)

        # Print the first line in the exact specified format
        print(f"Employee {employee_name} is done with tasks("
              f"{number_of_done_tasks}/{total_tasks}):")

        # Print the titles of completed tasks with 1 tabulation and 1 space
        for task in completed_tasks:
            # Get task title and strip any leading/trailing whitespace
            task_title = task.get('title', '').strip()
            print(f"\t {task_title}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")
    except ValueError:
        print("Error: Invalid JSON response from the API.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py "
              "<employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
