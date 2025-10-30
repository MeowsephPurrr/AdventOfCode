import csv


def csv_reader(file_path: str = 'data.csv'):
    csv_file = list()

    with open(file_path, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')

        for row in reader:
            tmp_row = list()
            for item in row:
                tmp_row.append(int(item))

            csv_file.append(tmp_row)

    return csv_file

def is_row_safe(row):
    if not (all_levels_are_increasing(row) or all_levels_are_decreasing(row)):
        return False

    if level_differ_to_much(row):
        return False


    return True


def all_levels_are_increasing(row):
    prev_item = -1 # we can assume the lowest level would be 0, which is always greater this value

    for item in row:
        if item > prev_item:
            prev_item = item
            continue

        return False

    return True

def all_levels_are_decreasing(row):
    prev_item = None

    for item in row:
        if not prev_item or item < prev_item:
            prev_item = item
            continue

        return False

    return True

def level_differ_to_much(row):
    min_diff = 1
    max_diff = 3

    prev_item = None

    for item in row:
        if not prev_item or min_diff <= abs(prev_item - item) <= max_diff:
            prev_item = item
            continue

        return True

    return False

if __name__ == '__main__':
    csv_data = csv_reader()
    number_of_safe_rows = 0

    for row in csv_data:
        if is_row_safe(row):
            number_of_safe_rows += 1

    print(number_of_safe_rows)