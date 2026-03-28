


print("project done by Mr. Danvish Anand\n")
print("i am doing todo list\n")
todo_list = []
def add_task(task):
    print("how many tasks do you want to add?")
    num_tasks = int(input("Enter how many tasks u want to do today:"))
    for i in range(num_tasks):
        task = input(f"enter task {i+1}: ")
        todo_list.append(task)
def view_tasks():
    print("your todo list:")
    for task in todo_list:
        print(task)
while True:
    print("what do you want to do? (1.add/2.view/3.exit 4.update)")
    choice = input()
    if choice == "1":
        add_task(todo_list)
        print("tasks added successfully")
        print("u r taskes are appended to the list",todo_list)
    elif choice == "2":
        print("u r tasks are:")
        view_tasks()
    elif choice == "3":
        break
    elif choice == "4":        
        print("enter the task you want to update:")
        old_task = input()
        if old_task in todo_list:
            print("enter the new task:")
            new_task = input()
            index = todo_list.index(old_task)
            todo_list[index] = new_task
            print("task updated successfully")
        else:
            print("task not found in the list")

    else:
        print("invalid choice, please try again")

n = int(input("enter the number of rows for the pattern: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

    