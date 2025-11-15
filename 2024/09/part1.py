def read_file_input():
    file = list()
    with open("data.txt") as f:
        for line in f:
            file.append(line)

    return file

def create_file_and_space_list(line: str) -> list:
    """
        Create a dict with starting index of block as index and value as value of the string
    """

    map = list()

    is_file = True
    file_number = "0"
    empty_char = "."
    for index, number in enumerate(line):
        if is_file:
            for _ in range(int(number)):
                map.append(file_number)
            is_file = False
            file_number = str(int(file_number) + 1)
        else:
            for _ in range(int(number)):
                map.append(empty_char)
            is_file = True

    return map

def swap_file_alloc(file_alloc: list) -> list:
    L = 0
    R = len(file_alloc) - 1

    empty_char = "."

    while L < R:
        if L < R and file_alloc[L] != empty_char:
            L += 1
            continue

        if L < R and file_alloc[R] == empty_char:
            R -= 1
            continue

        file_alloc[L], file_alloc[R] = file_alloc[R], file_alloc[L]

        L += 1
        R -= 1

    return file_alloc

def calculate_checksum(file_alloc: list) -> int:
    checksum = 0
    empty_char = "."

    for index, char in enumerate(list(file_alloc)):
        if char == empty_char:
            break
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

