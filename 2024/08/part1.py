import re

def read_file_input():
    file = list()
    with open("data.txt") as f:
        for line in f:
            tmp_line = list()
            for char in line:
                if char == "\n":
                    continue
                tmp_line.append(char)
            file.append(tmp_line)

    return file

def antenna_positions(antenna_regex: str, map: list) -> dict:
    antennas = dict()

    for row_index, row in enumerate(map):
        for col_index, col in enumerate(row):
            if antenna := re.match(antenna_regex, col):
                antenna = antenna.group()
                if not antenna in antennas:
                    antennas[antenna] = list()

                antennas[antenna].append((row_index, col_index))

    return antennas

def get_distance(first_position: tuple, second_position: tuple) -> tuple:
    return (first_position[0] - second_position[0]), (first_position[1] - second_position[1])

def get_antinodes(antennas: dict) -> list:
    antinodes = list()

    for antenna, positions in antennas.items():
        for first_position in positions:
            for second_position in positions:
                if first_position == second_position:
                    continue

                x, y = get_distance(first_position, second_position)

                if first_position[0] + x == second_position[0] and first_position[1] + y == second_position[1]:
                    pos_1 = (first_position[0] - x, first_position[1] - y)
                    pos_2 = (second_position[0] + x, second_position[1] + y)
                else:
                    pos_1 = (first_position[0] + x, first_position[1] + y)
                    pos_2 = (second_position[0] - x, second_position[1] - y)

                antinodes.append(pos_1)
                antinodes.append(pos_2)

    return antinodes

def remove_antinodes_outside_map(antinodes: list, height: int, width: int) -> list:
    tmp_antinodes = list()

    for node in antinodes:
        if 0 <= node[0] <= height and 0 <= node[1] <= width:
            tmp_antinodes.append(node)

    return tmp_antinodes


if __name__ == "__main__":
    map = read_file_input()
    map_height = len(map) - 1
    map_width = len(map[0]) - 1

    antenna_regex = r"(\d|\w)"

    antennas = antenna_positions(antenna_regex, map)

    antinodes = get_antinodes(antennas)

    antinodes = remove_antinodes_outside_map(antinodes, map_height, map_width)
    antinodes = list(set(antinodes))


    print("unique antinodes: ", len(antinodes))
