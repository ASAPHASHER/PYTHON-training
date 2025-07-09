import datetime
import time

def add_task(task_list, task_name, task_time):
    task_time_obj = datetime.datetime.strptime(task_time, "%H:%M").time()
    task_list.append({"name": task_name, "time": task_time_obj})

def schedule_tasks(task_list):
    # Sort the task list by time
    task_list.sort(key=lambda x: x["time"])
    print("\nYour Daily Schedule:")
    for task in task_list:
        print(f"{task['time'].strftime('%H:%M')} - {task['name']}")

def run_scheduler(task_list):
    print("\nStarting Task Scheduler...")
    for task in task_list:
        now = datetime.datetime.now().time()
        task_time = task["time"]

        # Calculate time to wait
        time_to_wait = (
            datetime.datetime.combine(datetime.date.today(), task_time) -
            datetime.datetime.combine(datetime.date.today(), now)
        ).total_seconds()

        if time_to_wait > 0:
            print(f"\nWaiting for task: {task['name']} at {task_time.strftime('%H:%M')}")
            time.sleep(time_to_wait)
            print(f"\n🔔 It's time for: {task['name']} ({task_time.strftime('%H:%M')})")
        else:
            print(f"\n⏩ Skipping past task: {task['name']} (already passed)")

# Example usage
if __name__ == "__main__":
    tasks = []

    # Add your tasks here
    add_task(tasks, "Morning Exercise", "07:00")
    add_task(tasks, "Breakfast", "08:00")
    add_task(tasks, "Study German", "09:30")
    add_task(tasks, "Lunch", "13:00")
    add_task(tasks, "Project Work", "15:00")
    add_task(tasks, "Evening Walk", "18:00")
    add_task(tasks, "Dinner", "20:00")

    schedule_tasks(tasks)

    # Uncomment this to enable real-time alerting
    # run_scheduler(tasks)
