import re

if __name__ == '__main__':
    do_regex = r"do\\\(\\\)"
    dont_regex = r"don\'t\\\(\\\)"
    instruction_regex = r"(do\\\(\\\)|don\'t\\\(\\\)|mul\\\(\d+,\d+\\\))"
    instructions = list()
    with open('data.txt') as f:
        lines = re.escape(f.read().strip())
        instructions.extend(re.findall(instruction_regex, lines))

    solution = 0
    skip_following_instructions = False
    for item in instructions:

        if re.match(do_regex, item):
            skip_following_instructions = False
            continue

        if re.match(dont_regex, item):
            skip_following_instructions = True
            continue

        if skip_following_instructions:
            continue

        numbers = re.findall(r"\d+", item)
        solution += int(numbers[0]) * int(numbers[1])

    print(solution)


