tail = input()
body = input()
head = input()

zoo_list = [tail, body, head]
zoo_list[0], zoo_list[2] = zoo_list[2], zoo_list[0]
print(zoo_list)