from service import TaskService


def seed_demo_data(service: TaskService):
    service.add_task("Prepare demo slides", "high", "2026-05-30")
    service.add_task("Write unit tests", "medium", "2026-05-31")
    service.add_task("Update README", "low")
    service.complete_task(2)


def main():
    service = TaskService()
    seed_demo_data(service)

    print("All tasks:")
    for task in service.list_tasks():
        print(task)

    print("\nPending tasks:")
    for task in service.list_tasks("pending"):
        print(task)

    print("\nSummary:")
    print(service.summary())


if __name__ == "__main__":
    main()