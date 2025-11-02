def term_equals_search(term, search_terms=None):
    if search_terms is None:
        search_terms = ["XMAS", "SAMX"]
    if term in search_terms:
        return True
    return False


if __name__ == '__main__':
    count_of_xmas = 0

    vert_count = 0
    hori_count = 0
    dia_count_r = 0
    dia_count_l = 0

    lines = list()
    with open('data.txt') as f:
        for line in f:
            lines.append(line.strip())

    rows = len(lines)
    cols = len(lines[0])

    cur_rowindex = 0
    cur_colindex = 0

    while cur_rowindex < rows:
        while cur_colindex < cols:
            row_string = ""
            """ go from top to bottom in a single column """
            for i in range(0, 4):
                if cur_rowindex + i < rows:
                    row_string += lines[cur_rowindex + i][cur_colindex]

            if term_equals_search(row_string):
                vert_count += 1
            """ end """

            """ go from left to right in a single row """
            col_string = ""
            for i in range(0, 4):
                if cur_colindex + i < cols:
                    col_string += lines[cur_rowindex][cur_colindex + i]

            if term_equals_search(col_string):
                hori_count += 1
            """ end """

            """ go from top left to bottom right """
            right_dia_string = ""
            for i in range(0, 4):
                if cur_rowindex + i < rows and cur_colindex + i < cols:
                    right_dia_string += lines[cur_rowindex + i][cur_colindex + i]

            if term_equals_search(right_dia_string):
                dia_count_r += 1
            """ end """

            """ go from top right to bottom left """
            left_dia_string = ""
            for i in range(0, 4):
                if cur_rowindex + i < rows and 0 <= cur_colindex - i:
                    left_dia_string += lines[cur_rowindex + i][cur_colindex - i]

            if term_equals_search(left_dia_string):
                dia_count_l += 1
            """ end """

            cur_colindex += 1

        cur_colindex = 0
        cur_rowindex += 1

    print("vert:", vert_count)
    print("hori:", hori_count)
    print("dia_l: ", dia_count_l)
    print("dia_r: ", dia_count_r)
    print(vert_count + hori_count + dia_count_r + dia_count_l)
