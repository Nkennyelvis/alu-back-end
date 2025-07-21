
#!/usr/bin/python3


import sys
import requests


def fetch_user(user_id):
    """Fetch user data from API."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_todos(user_id):
    """Fetch TODO tasks for a given user."""
    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    response.raise_for_status()
    return response.json()


def get_task_summary(tasks):
    """Return a tuple with number of completed tasks and their titles."""
    completed = [task["title"] for task in tasks if task.get("completed")]
    return len(completed), len(tasks), completed


def display_progress(user, done_count, total_count, completed_titles):
    """Print the progress report."""
    print(f"Employee {user['name']} is done with tasks({done_count}/{total_count}):")
    for title in completed_titles:
        print(f"\t {title}")


def main():
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress_checker.py <employee_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    try:
        user = fetch_user(user_id)
        todos = fetch_todos(user_id)
        done, total, completed_titles = get_task_summary(todos)
        display_progress(user, done, total, completed_titles)

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
