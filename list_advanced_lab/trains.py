numbers_of_wagons = int(input())
train = [0] * numbers_of_wagons

command = input()

while command != "End":
    action = command.split()[0]
    if action == "add":
       num_of_people = int(command.split()[1])
       train[-1] += num_of_people
    elif action == "insert":
        index = int(command.split()[1])
        num_of_people = int(command.split()[2])
        train[index] += num_of_people
    elif action == "leave":
        index = int(command.split()[1])
        num_of_people = int(command.split()[2])
        train[index] -= num_of_people
    command = input()

print(train)
