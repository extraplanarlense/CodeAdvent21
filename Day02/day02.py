import re

def load_data(filename):
    with open(filename, mode="rt") as input:
        lines = list(map(str, input.readlines()))
        converted_lines = []
        for element in lines:
            converted_lines.append(element.strip())
    return converted_lines

def calc_progress(data):
    horizontal = 0
    depth = 0
    for element in data:
        command = ''.join([i for i in element if not i.isdigit()])
        number = re.sub(r'[a-z]+', '', element, re.I).strip()
        if command == "forward ":
            horizontal += int(number)
        elif command == "up ":
            depth -= int(number)
        elif command == "down ":
            depth += int(number)
    return horizontal, depth

def calc_progress_aim(data):
    horizontal = 0
    aim = 0
    depth = 0
    for element in data:
        command = ''.join([i for i in element if not i.isdigit()])
        number = re.sub(r'[a-z]+', '', element, re.I).strip()
        if command == "forward ":
            horizontal += int(number)
            depth += int(aim) * int(number)
        elif command == "up ":
            aim -= int(number)
        elif command == "down ":
            aim += int(number)
    return horizontal, depth

if __name__ == '__main__':
    data = load_data("input.txt")
    horizontal, depth = calc_progress(data)
    horizontal_aim, depth_aim = calc_progress_aim(data)
    print (horizontal, ", ", depth, " = ", horizontal * depth)
    print (horizontal_aim, ", ", depth_aim, "[with aim] = ", horizontal_aim * depth_aim)