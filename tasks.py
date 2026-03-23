from datetime import datetime
from storage import load_json, save_json, get_task_file


def get_next_task_id(tasks):
    return max([t["id"] for t in tasks], default=0) + 1


def sort_tasks(tasks):
    return sorted(tasks, key=lambda x: x["status"] == "Completed")


def add_task(username, description):
    if not description.strip():
        return False, "Task cannot be empty"

    file = get_task_file(username)
    tasks = load_json(file)

    task_id = get_next_task_id(tasks)

    tasks.append({
        "id": task_id,
        "task": description,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    save_json(file, tasks)
    return True, f"Task added (ID: {task_id})"


def load_tasks(username):
    return load_json(get_task_file(username))


def mark_task_completed(username, task_id):
    tasks = load_tasks(username)

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_json(get_task_file(username), tasks)
            return True, "Task marked completed"

    return False, "Task ID not found"


def delete_task(username, task_id):
    tasks = load_tasks(username)
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == len(new_tasks):
        return False, "Task ID not found"

    save_json(get_task_file(username), new_tasks)
    return True, "Task deleted"