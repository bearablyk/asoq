import multiprocessing
import time
from asoq import task, start_worker


@task()
def send_notification(user_id: int, message: str):
    print(f"WORKER: Starting to send notification to user {user_id}...")
    time.sleep(5)  # Імітація довгої роботи
    print(f"WORKER: Notification '{message}' sent to user {user_id}.")


@task()
def another_task():
    print("WORKER: Executing another simple task...")
    time.sleep(1)
    print("WORKER: Another task finished.")


def main():
    print(f"Main process started with PID: {multiprocessing.current_process().pid}")
    start_worker()

    time.sleep(1)

    print("MAIN: Simulating first API request.")
    send_notification.delay(user_id=123, message="Your order is shipped!")

    print("MAIN: Simulating second API request.")
    another_task.delay()

    print("MAIN: Both tasks enqueued. Main process continues...")

    time.sleep(10)
    print("MAIN: Main process finished.")


if __name__ == "__main__":
    main()

