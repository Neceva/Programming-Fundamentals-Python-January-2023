number_of_rooms = int(input())
list_chairs = []
free_chairs = 0
is_free_chairs = True
for room in range(1, number_of_rooms + 1):
    list_chairs.clear()
    chairs, visitors = input().split()
    list_chairs.append(chairs)
    visitors = int(visitors)
    if visitors > len(chairs):
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")
        is_free_chairs = False
    elif visitors < len(chairs):
        free_chairs += len(chairs) - visitors

if is_free_chairs:
    print(f"Game On, {free_chairs} free chairs left")
