if __name__ == '__main__':
    with open('input.data') as f:
        numbers_string  = f.readlines()
    integer_map = map(int, numbers_string)
    numbers = list(integer_map)
    counter = 0
    buffer = -1
    for current_number in numbers:
        if (buffer != -1):
            if current_number > buffer:
                counter += 1
            buffer = current_number
        else:
            buffer = current_number
    print(counter)



