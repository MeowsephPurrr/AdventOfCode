import math

if __name__ == '__main__':
    rules = list()
    updates = list()
    with open('rules.txt') as f:
        for line in f:
            rule = line.strip().split('|')
            rules.append(rule)

    with open('updates.txt') as f:
        for line in f:
            update = line.strip().split(',')
            updates.append(update)

    # A map constisting of a key and all the numbers which must come after and before it
    rule_map = dict()

    for rule in rules:
        if rule[0] not in rule_map:
            rule_map[rule[0]] = {'before': [], 'after': []}

        rule_map[rule[0]]['after'].append(rule[1])

        if rule[1] not in rule_map:
            rule_map[rule[1]] = {'before': [], 'after': []}

        rule_map[rule[1]]['before'].append(rule[0])


    accepted_updates = list()
    for row in updates:
        succ = False
        for index, number in enumerate(row):
            before = rule_map[number]['before']
            after = rule_map[number]['after']

            # check if a number from the after rules is before this number
            if index > 0 and bool(set(after) & set(row[:index-1])):
                succ = False
                break

            # check if a number from the before rules is after this number
            if index < (len(row) -1) and bool(set(before) & set(row[index + 1:])):
                succ = False
                break

            succ = True

        if succ:
            accepted_updates.append(row)

    accepted_updates_number = 0
    for update in accepted_updates:
        middle_number = update[math.floor(len(update) / 2)]
        accepted_updates_number += int(middle_number)

    print(accepted_updates_number)