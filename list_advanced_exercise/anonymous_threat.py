first_input_line = input().split()
instructions = input()
while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(first_input_line) - 1:
            end_index = len(first_input_line) - 1
        for index, string in enumerate(first_input_line):
            if index in range(start_index + 1, end_index + 1):
                first_input_line[start_index] += first_input_line[index]

# first_input_line = input().split()
# result = []
# instructions = input()
# while not instructions == "3:1":
#     instructions = instructions.split()
#     command = instructions[0]
#     if command == 'merge':
#         start = int(instructions[1])
#         end = int(instructions[2])
#         if start < 0:
#             start = 0
#         if end > len(first_input_line) - 1:
#             end = len(first_input_line) - 1
#         for index, string in enumerate(first_input_line):
#             if index in range(start + 1, end + 1):
#                 first_input_line[start] += first_input_line[index]
#         for index in range(end, start, - 1):
#             first_input_line.pop(index)
#     elif command == 'divide':
#         index = int(instructions[1])
#         partitions = int(instructions[2])
#         if partitions > len(first_input_line[index]):
#             step = 1
#         else:
#             step = len(first_input_line[index]) // partitions
#         divide_part = first_input_line.pop(index)
#         start = 0
#         for parts in range(partitions):
#             if parts == partitions - 1:
#                 first_input_line.insert(index, divide_part[start::])
#                 break
#             else:
#                 first_input_line.insert(index, divide_part[start: start + step:])
#             start += step
#             index += 1
#     instructions = input()
# print(' '.join(first_input_line))