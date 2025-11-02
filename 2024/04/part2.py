import re

def term_equals_search(term, search_terms=None):
    if search_terms is None:
        search_terms = ["MAS", "SAM"]
    if term in search_terms:
        return True
    return False


if __name__ == '__main__':
    count_of_xmas = 0

    lines = list()
    with open('data.txt') as f:
        for line in f:
            lines.append(line.strip())

    rows = len(lines)
    cols = len(lines[0])

    cur_rowindex = 0
    cur_colindex = 0
    while cur_rowindex < rows:
        if cur_rowindex == 0 or cur_rowindex == rows - 1:
            cur_rowindex += 1
            continue

        while cur_colindex < cols:
            if cur_colindex == 0 or cur_colindex == cols - 1:
                cur_colindex += 1
                continue

            dia_string_r = ""
            dia_string_l = ""

            for i in range(-1, 2):
                try:
                    dia_string_r += lines[cur_rowindex + i][cur_colindex + i]
                    dia_string_l += lines[cur_rowindex + i][cur_colindex - i]
                except:
                    break

            if dia_string_r != "" and dia_string_l != "" and term_equals_search(dia_string_l) and term_equals_search(dia_string_r):
                print("r: ", cur_rowindex, "l:", cur_colindex)
                count_of_xmas += 1

            cur_colindex += 1

        cur_colindex = 0
        cur_rowindex += 1

    print(count_of_xmas)
