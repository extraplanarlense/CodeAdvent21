def load_data(filename):
    with open(filename) as f:
        raw_data = f.read().split()
    return raw_data


def extract_bingo_numbers(data):
    return list(data[0].split(','))


def create_bingo_tables(data):
    board_count = len(data)
    tables = [[[[0, 0] for x in range(5)] for x in range(5)] for x in range(board_count)]
    for count, value in enumerate(data[1:]):
        table_number = count // 25
        item_column = count % 5
        item_row = (count // 5) % 5
        tables[table_number][item_column][item_row] = [value, 0]
        #print("table number: ", table_number, "item column: ", item_column, "item row: ", item_row, "value: ", value)
    return tables


def draw_numbers(bingo_numbers, bingo_tables):
    winner = 0
    winner_board = 0
    board_count = len(bingo_tables)
    for current_number in bingo_numbers:
        for current_board in range(board_count):
            for current_row in range(5):
                for current_column in range(5):
                    if bingo_tables[current_board][current_column][current_row][0] == current_number:
                        #print(current_board, "current_column :", current_column, "current_row:", current_row, "current_number: ", current_number)
                        bingo_tables[current_board][current_column][current_row][1] = 1
                        if ((bingo_tables[current_board][0][current_row][1] ==
                            bingo_tables[current_board][1][current_row][1] ==
                            bingo_tables[current_board][2][current_row][1] ==
                            bingo_tables[current_board][3][current_row][1] ==
                            bingo_tables[current_board][4][current_row][1] == 1) or
                            bingo_tables[current_board][current_column][0][1] ==
                            bingo_tables[current_board][current_column][1][1] ==
                            bingo_tables[current_board][current_column][2][1] ==
                            bingo_tables[current_board][current_column][3][1] ==
                            bingo_tables[current_board][current_column][4][1] == 1):
                                winner_board = current_board
                                print("Winner!!! On board:", winner_board + 1, current_number)
                                winning_sum = 0
                                for row in range(5):
                                    for column in range(5):
                                        if bingo_tables[current_board][column][row][1] == 0:
                                            winning_sum += int(bingo_tables[current_board][column][row][0])
                                return winning_sum * int(current_number)

if __name__ == '__main__':
    raw_data = load_data("input.txt")
    bingo_numbers = extract_bingo_numbers(raw_data)
    bingo_tables = create_bingo_tables(raw_data)
    print(draw_numbers(bingo_numbers, bingo_tables))
