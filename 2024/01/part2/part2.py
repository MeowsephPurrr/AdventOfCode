import csv

def map_value_to_count(value, count_dict):
    if value in count_dict:
        count_dict[value] += 1
        return

    count_dict[value] = 1

def get_count_and_iterator_lists(csv_file_path='../data.csv'):
    iterator_list = list()
    count_dict = {}
    with open(csv_file_path, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        for row in reader:
            iterator_list.append(int(row[0]))
            map_value_to_count(int(row[1]), count_dict)

    return count_dict, iterator_list

def get_value_counter(count_dict, iterator_item):
    if not iterator_item in count_dict:
        return 0

    return count_dict[iterator_item] * iterator_item


if __name__ == '__main__':
    solution = 0

    count_dict, iterator_list = get_count_and_iterator_lists()
    for iterator_item in iterator_list:
        solution += get_value_counter(count_dict, iterator_item)

    print(solution)