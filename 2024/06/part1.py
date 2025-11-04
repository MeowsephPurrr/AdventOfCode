class Direction:
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    TRANSITIONS = {
        NORTH: EAST,
        EAST: SOUTH,
        SOUTH: WEST,
        WEST: NORTH,
    }

def target_move_distance(move_direction):
    row_move = 0
    col_move = 0
    match move_direction:
        case Direction.NORTH:
            row_move = -1
        case Direction.SOUTH:
            row_move = 1
        case Direction.EAST:
            col_move = 1
        case Direction.WEST:
            col_move = -1

    return row_move, col_move


if __name__ == '__main__':
    GUARD = '^'
    BLOCKAGE = '#'
    VISITED = 'X'

    move_direction = Direction.NORTH
    visited_fields = 0

    map_layout = list()
    with open('data.txt') as f:
        for line in f:
            row = list()
            for char in line.strip():
                row.append(char)
            map_layout.append(row)


    row_index = 0
    col_index = 0
    for index, row in enumerate(map_layout):
        try:
            col_index = row.index(GUARD)
            row_index = index
            break
        except:
            pass

    cur_row_index = row_index
    cur_col_index = col_index

    while 0 <= cur_row_index < len(map_layout) and 0 <= cur_col_index < len(map_layout[0]):
        map_layout[cur_row_index][cur_col_index] = VISITED

        while True:
            row_move, col_move = target_move_distance(move_direction)

            if map_layout[cur_row_index + row_move][cur_col_index + col_move] == BLOCKAGE:
                move_direction = Direction.TRANSITIONS[move_direction]
                continue

            cur_row_index += row_move
            cur_col_index += col_move
            break

    for row in map_layout:
        string_row = "".join(row)
        visited_fields += string_row.count(VISITED)

    print(visited_fields)