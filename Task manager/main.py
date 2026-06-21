from logic import add_task, show_tasks, complete_task, delete_task, save_tasks, load_tasks,  get_tasks_by_status, search_tasks, edit_task, get_stats, sort_tasks_by_priority, edit_due_date, get_tasks_by_priority, get_overdue_tasks, string_to_date


def main():
    tasks = load_tasks()

    valid_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

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
        print("12. Edit due date")
        print("13 Show tasks by Priority")
        print("14 Filter task by status")
        print("15 Show overdue tasks")

        option = input("Choose: ")
        option = option.strip()


        if option not in valid_options:
            print("Invalid option")
            continue

        if option == "1":
            title = input("Task title: ")
            priority = input("Priority: ")
            priority = priority.strip()
            priority = priority.title()

            due_date = input("Due_date: ")

            try:
                string_to_date(due_date)

                add_task(tasks, title, priority, due_date)
                save_tasks(tasks)

            except:
                print("invalid date. Use YYYY-MM-DD")

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

        elif option == "12":
            show_tasks(tasks)

            index = int(input("Enter tasks index: "))
            new_due_date = input("New due date: ")

            try:
                string_to_date(new_due_date)
            except: 
                print("Invalid date")
                continue

            try:
                index = int(input("Index: "))
            except:
                print("Invalid index")
                continue

            edit_due_date(tasks, index, new_due_date)
            save_tasks(tasks)

        elif option == "13":
            priority = input("Enter priority (High, Medium, Low): ")

            priority_tasks = get_tasks_by_priority(tasks, priority)
            show_tasks(priority_tasks)

        elif option == "14":        
            status = input("Enter status (completed/pending): ").lower()

            if status == "completed":
                target_status = True
            elif status == "pending":
                target_status = False
            else:
                print("Invalid Status")
                continue

            filtered_tasks = get_tasks_by_status(tasks, target_status)
            show_tasks(filtered_tasks)

        elif option == "15":
            overdue_tasks = get_overdue_tasks(tasks)
            show_tasks(overdue_tasks)

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()