from logic import add_task, show_tasks, complete_task, delete_task, save_tasks, load_tasks


def main():
    tasks = load_tasks()

    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        option = input("Choose: ")

        if option == "1":
            title = input("Task title: ")

            add_task(tasks, title)
            save_tasks(tasks)

        elif option == "2":
            show_tasks(tasks)

        elif option == "3":
            show_tasks(tasks)

            try:
                index = int(input("Enter task index to complete: "))
            except:
                print("Invalid number")
                continue

            complete_task(tasks, index)
            save_tasks(tasks)

        elif option == "4":
            show_tasks(tasks)

            try:
                index = int(input("Enter task index to delete: "))
            except:
                print("Invalid number")
                continue

            delete_task(tasks, index)
            save_tasks(tasks)

        elif option == "5":
            print("Goodbye")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()