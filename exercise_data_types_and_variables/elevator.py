import math
number_of_people = int(input())
capacity = int(input())
number_of_full_courses = math.ceil(number_of_people / capacity)

print(math.ceil(number_of_full_courses))
