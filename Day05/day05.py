import sys

if __name__ == '__main__':

    with open("input.txt", mode="rt") as input:
        lines = input.read().splitlines()

    lines = [l.split("->") for l in lines]
    lines = [tuple(tuple(map(int, item.strip().split(","))) for item in l) for l in lines]
    max_x = max(max(x1, x2) for (x1, _y1), (x2, _y2) in lines)
    max_y = max(max(y1, y2) for (_x1, y1), (_x2, y2) in lines)

    array = [[0 for _y in range(max_y + 1)] for _x in range(max_x + 1)]

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                array[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                array[x][y1] += 1
        elif (x1 - x2 == y1 - y2):
            x_min = min(x1, x2)
            y_min = min(y1, y2)
            for d in range(abs(x1 - x2) + 1):
                array[x_min +d][y_min + d] += 1
        elif (x1 - x2 == y2 - y1):
            x_min = min(x1, x2)
            y_max = max(y1, y2)
            for d in range(abs(x1 - x2) + 1):
                array[x_min +d][y_max - d] += 1


    # print(*array, sep="\n")

    result = 0
    for column in array:
        for cell in column:
            if cell >= 2:
                result += 1

    print(result)
