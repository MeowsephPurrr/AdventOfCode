def read_file_input():
    file = list()
    with open("data.txt") as f:
        for line in f:
            file.append(line)

    return file


def create_file_and_space_list(line: str) -> list:
    map = list()

    is_file = True
    file_number = "0"
    empty_char = "."
    for index, number in enumerate(line):
        tmp = list()
        if is_file:
            for _ in range(int(number)):
                tmp.append(file_number)
            map.append(tmp)
            is_file = False
            file_number = str(int(file_number) + 1)
        else:
            for _ in range(int(number)):
                tmp.append(empty_char)
            map.append(tmp)
            is_file = True

    return map


def is_empty_space(space: list) -> bool:
    empty_char = "."
    return empty_char in space or not space


def try_swapping_space(file_alloc: list, L: int, R: int) -> list:
    left_len = len(file_alloc[L])
    right_len = len(file_alloc[R])
    if left_len == right_len:
        file_alloc[L], file_alloc[R] = file_alloc[R], file_alloc[L]
    else:
        swapping_space, rest_of_free_space = file_alloc[L][:right_len], file_alloc[L][right_len:]
        file_alloc[L], file_alloc[R] = file_alloc[R], swapping_space
        file_alloc.insert(L+1, rest_of_free_space)

    return file_alloc


def fix_empty_spaces(file_alloc: list) -> list:
    L = 0
    while L + 1 < len(file_alloc):
        if is_empty_space(file_alloc[L]) and is_empty_space(file_alloc[L+1]):
            file_alloc[L] += file_alloc[L+1]
            file_alloc.pop(L+1)
            continue

        L += 1
    return file_alloc


def get_matching_left_space_position(file_alloc: list, R: int) -> int:
    L = 0
    while L <= R:
        if not is_empty_space(file_alloc[L]):
            L += 1
            continue

        if len(file_alloc[L]) >= len(file_alloc[R]):
            break

        L += 1

    return L

def swap_file_alloc(file_alloc: list) -> list:
    R = len(file_alloc) - 1
    while R >= 0:
        if is_empty_space(file_alloc[R]):
            R -= 1
            continue

        new_left_space_position = get_matching_left_space_position(file_alloc, R)
        if new_left_space_position >= R:
            R -= 1
            continue

        file_alloc = try_swapping_space(file_alloc, new_left_space_position, R)
        file_alloc = fix_empty_spaces(file_alloc)

        R -= 1

    return file_alloc


def calculate_checksum(file_alloc: list) -> int:
    checksum = 0
    empty_char = "."
    flat_list = [
        x
        for xs in file_alloc
        for x in xs
    ]

    for index, char in enumerate(list(flat_list)):
        if char == empty_char:
            continue
        checksum += index * int(char)

    return checksum


def write_to_file(s: str):
    with open("tmp.txt", "a") as f:
        f.write(s)
        f.write('\n')


if __name__ == "__main__":
    file = read_file_input()
    line = file[0]

    alloc_list = create_file_and_space_list(line)
    swapped_file_alloc = swap_file_alloc(alloc_list)

    checksum = calculate_checksum(swapped_file_alloc)
    print(checksum)
