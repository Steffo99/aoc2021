with open("input.dat") as file:
    commands = map(lambda l: l.split(" "), map(lambda l: l.rstrip("\n"), file.readlines()))

h_pos = 0
depth = 0
aim = 0


for command, value in commands:
    value = int(value)
    if command == "forward":
        h_pos += value
        depth += aim * value
    if command == "up":
        aim -= value
    if command == "down":
        aim += value


print(depth * h_pos)
