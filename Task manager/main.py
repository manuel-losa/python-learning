from logic import add_task, show_tasks, complete_task, delete_task, save_tasks, load_tasks,  get_tasks_by_status, search_tasks, edit_task, get_stats, sort_tasks_by_priority


def main():
    tasks = load_tasks()

    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        print("6. Show pending tasks")
        print("7. Show completed tasks")
        print("8. Search")
        print("9. Edit task")
        print("10. Get stats")
        print("11. Sort by priority")

        option = input("Choose: ")

        if option == "1":
            title = input("Task title: ")
            priority = input("Priority: ")

            add_task(tasks, title, priority)
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

        elif option == "6":
            filtered_tasks = get_tasks_by_status(tasks, False)
            show_tasks(filtered_tasks)

        elif option == "7":
            filtered_tasks = get_tasks_by_status(tasks, True)
            show_tasks(filtered_tasks)

        elif option == "8":
            search = input("Search: ")

            matched_tasks = search_tasks(tasks, search)

            if len(matched_tasks) == 0:
                print("Not matching tasks found")
            else:
                show_tasks(matched_tasks)

        elif option == "9":
            show_tasks(tasks)

            index = int(input("Enter task index: "))
            new_title = input("New title: ")

            edit_task(tasks, index, new_title)

            save_tasks(tasks)

        elif option == "10":
            
            completed, pending = get_stats(tasks)

            print(f"Total tasks: {len(tasks)}")
            print(f"Completed: {completed}")
            print(f"Pending: {pending}")

        elif option == "11":
            tasks = sort_tasks_by_priority(tasks)
            save_tasks(tasks)
            show_tasks(tasks)

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()