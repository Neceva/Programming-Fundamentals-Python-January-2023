waiting_people = int(input())
lift_state = [int(element) for element in input().split()]

for index in range(len(lift_state)):
    can_load = min(4 - lift_state[index], waiting_people)
    lift_state[index] += can_load
    waiting_people -= can_load

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
elif len([element for element in lift_state if element < 4]) > 0:
    print("The lift has empty spots!")

print(" ".join([str(element) for element in lift_state]))