import re


class Node:
    value: int

    add: "Node | None"
    mul: "Node | None"

    def __init__(self, value: int):
        self.value = value
        self.add = None
        self.mul = None

    def set_add(self, value: int):
        val = self.value + value
        self.add = Node(val)

    def set_mul(self, value: int):
        val = self.value * value
        self.mul = Node(val)

    def is_leaf_matching_target_result(self, target_result: int) -> bool:
        if self.add is None and self.mul is None:
            return self.value == target_result

        return (self.add.is_leaf_matching_target_result(target_result)
                or self.mul.is_leaf_matching_target_result(target_result))


def read_file_input():
    file = list()
    with open("data.txt") as f:
        for line in f:
            file.append(line)

    return file


def get_result_and_numbers(line: str) -> tuple[int, list[int]]:
    found_numbers = re.findall(r"\d+", line)
    result = int(found_numbers[0])
    numbers = list()
    for number in found_numbers[1:]:
        numbers.append(int(number))

    return result, numbers


def create_tree(node, numbers, index):
    try:
        current_number = numbers[index]
        next_index = index + 1

        node.set_add(current_number)
        create_tree(node.add, numbers, next_index)

        node.set_mul(current_number)
        create_tree(node.mul, numbers, next_index)
    except:
        pass


def get_calibration_value(target_result: int, numbers: list[int]) -> int:
    sum = 0

    first_node = Node(value=numbers[0])
    create_tree(first_node, numbers, 1)

    if first_node.is_leaf_matching_target_result(target_result):
        sum += target_result

    return sum


if __name__ == "__main__":
    file = read_file_input()

    sum = 0
    for line in file:
        result, numbers = get_result_and_numbers(line)
        sum += get_calibration_value(result, numbers)

    print(sum)
