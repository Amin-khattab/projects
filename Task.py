num_tasks = int(input("how many tasks do you want ?"))

list_of_tasks = {}

for i in range(num_tasks):
    task = input(f"what is the {i+1} task ? ").lower()
    priority = input("what is this tasks priority ? ").lower()
    list_of_tasks[task] = priority

completed_tasks = {}

while True:
    print("input 'exit' if you want to get out")
    user_completed_tasks = input(" what task did you complete ").lower()

    if user_completed_tasks =="exit":
        break

    if user_completed_tasks in list_of_tasks:
        completed_tasks[user_completed_tasks] =  list_of_tasks[user_completed_tasks]
        del list_of_tasks[user_completed_tasks]
        print(f"completed tasks are now {completed_tasks}")
    else:
        print(f"this task {user_completed_tasks} wasnt found")
        continue

    print("input 'exit' to exit the loop")
    user_delete_task = input("what task do you want to delete ? ").lower()

    if "exit" in user_delete_task:
        break

    if user_delete_task in list_of_tasks:
        del list_of_tasks[user_delete_task]
        print(f"task {user_delete_task} has been deleted")
    else:
        print(f" task {user_delete_task} wasnt found ")

    print(f"remaining tasks {list_of_tasks}")
