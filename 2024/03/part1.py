import re

if __name__ == '__main__':
    mul_regex = r"mul\\\(\d+,\d+\\\)"
    mults = list()
    with open('data.txt') as f:
        lines = re.escape(f.read().strip())
        mults.extend(re.findall(mul_regex, lines))

    solution = 0
    for item in mults:
        numbers = re.findall(r"\d+", item)
        solution += int(numbers[0]) * int(numbers[1])

    print(solution)