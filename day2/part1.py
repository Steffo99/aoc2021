with open("input.dat") as file:
    commands = map(lambda l: l.split(" "), map(lambda l: l.rstrip("\n"), file.readlines()))

h_pos = 0
depth = 0


for command, value in commands:
    value = int(value)
    if command == "forward":
        h_pos += value
    if command == "up":
        depth -= value
    if command == "down":
        depth += value


print(depth * h_pos)
