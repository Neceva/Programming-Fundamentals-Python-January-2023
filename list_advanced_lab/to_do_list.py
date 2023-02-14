to_do_list = []
command = input()

while command != "End":
    split_command = command.split("-")
    priority = int(split_command[0])
    current_task = split_command[1]
    to_do_list.append((priority, current_task))
    command = input()

sorted_tasks = [task_data[1] for task_data in sorted(to_do_list)]
print(sorted_tasks)