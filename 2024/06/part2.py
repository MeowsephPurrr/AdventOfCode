import copy


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

def get_map_layout():
    map_layout = list()
    with open('data.txt') as f:
        for line in f:
            row = list()
            for char in line.strip():
                row.append(char)
            map_layout.append(row)

    return map_layout

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

def do_step(map, cur_row_index, cur_col_index, move_direction):
    if map[cur_row_index][cur_col_index] == UNVISITED:
        map[cur_row_index][cur_col_index] = move_direction
    else:
        map[cur_row_index][cur_col_index] += move_direction

    return map

def get_turn_and_step(map, cur_row_index, cur_col_index, move_direction):
    while True:
        row_move, col_move = target_move_distance(move_direction)

        if map[cur_row_index + row_move][cur_col_index + col_move] == BLOCKAGE:
            move_direction = Direction.TRANSITIONS[move_direction]
            continue

        cur_row_index += row_move
        cur_col_index += col_move
        break

    return cur_row_index, cur_col_index, move_direction

def is_block_possible(map, cur_row_index, cur_col_index, move_direction):
    tmp_move = copy.copy(move_direction)
    try:
        # one interation of the loop is a step
        while 0 <= cur_row_index < len(map) and 0 <= cur_col_index < len(map[0]):

            map = do_step(map, cur_row_index, cur_col_index, move_direction)

            tmp_cur_row_index, tmp_cur_col_index, move_direction = get_turn_and_step(map, cur_row_index, cur_col_index, move_direction)

            if tmp_move != move_direction:
                print('change move dir from', tmp_move, 'to', move_direction)
                tmp_move = move_direction

            if move_direction in map[tmp_cur_row_index][tmp_cur_col_index]:
                print('')
                draw_map(map)
                print('')
                return True

            cur_row_index = tmp_cur_row_index
            cur_col_index = tmp_cur_col_index
    except:
        pass
    return False

def move_through_map(map: list, cur_row_index: int, cur_col_index: int, move_direction: str, copied=False):
    possible_blocks = 0
    try:
        # one interation of the loop is a step
        while 0 <= cur_row_index < len(map) and 0 <= cur_col_index < len(map[0]):
            map = do_step(map, cur_row_index, cur_col_index, move_direction)

            if not copied:
                copied_map = copy.deepcopy(map)
                next_row_move, next_col_move = target_move_distance(move_direction)
                if copied_map[cur_row_index + next_row_move][cur_col_index + next_col_move] == UNVISITED and not (cur_row_index + next_row_move == guard_starting_row_index and cur_col_index + next_col_move == guard_starting_col_index):
                    copied_map[cur_row_index + next_row_move][cur_col_index + next_col_move] = BLOCKAGE
                    is_blockable = is_block_possible(copied_map, cur_row_index, cur_col_index, move_direction)
                    if is_blockable:
                        return map, 0
                        possible_blocks += 1

            tmp_cur_row_index, tmp_cur_col_index, move_direction = get_turn_and_step(map, cur_row_index, cur_col_index, move_direction)
            if map[tmp_cur_row_index][tmp_cur_col_index] == move_direction:
                return map, possible_blocks + 1

            cur_row_index = tmp_cur_row_index
            cur_col_index = tmp_cur_col_index
            print('possible blocks: ',possible_blocks)
    except:
        pass

    return map, possible_blocks

def get_starting_guard_position(map):
    GUARD = '^'
    row_index = 0
    col_index = 0
    for index, row in enumerate(map):
        try:
            col_index = row.index(GUARD)
            row_index = index
            break
        except:
            pass

    return row_index, col_index

def draw_map(map: list):
    for row in map:
        string_row = "".join(row)
        print(string_row)


if __name__ == '__main__':
    print('doing stuff')
    BLOCKAGE = '#'
    UNVISITED = '.'

    move_direction = Direction.NORTH

    map_layout = get_map_layout()
    guard_starting_row_index, guard_starting_col_index = get_starting_guard_position(map_layout)
    move_map, possible_blocks = move_through_map(map_layout, guard_starting_row_index, guard_starting_col_index, move_direction)

    #draw_map(move_map)

    print(possible_blocks)