from logic import add_task, show_tasks, complete_task, delete_task


def main():
    tasks = []

    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("4. Exit")


        option = input("Choose: ")

        if option == "1":
            title = input("Task title: ")
            add_task(tasks, title)

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

        elif option == "4":
            show_tasks(tasks)

            try:
                index = int(input("Enter task index to delete: "))
            except: 
                print("Invalid number")
                continue

            delete_task(tasks, index)

        elif option == "5":
            print("Good bye")
            break
        
        else: 
            print("Invalid option")

        
if __name__ == "__main__":
    main()