stops = input()

while True:
    line = input()
    if line == "Travel":
        break
    instruction = line.split(":")
    if "Add Stop" in instruction:
        index = int(instruction[1])
        string = instruction[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif "Remove Stop" in instruction:
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    if "Switch" in instruction:
        old_string = instruction[1]
        new_string = instruction[2]
        stops = stops.replace(old_string, new_string)
        print(stops)
print(f"Ready for world tour! Planned stops: {stops}")