import math

def fix_row(failed_rules: set, row: list, index: int) -> list:
    failed_rules = list(failed_rules)

    for item in tmp_row[index + 1:]:
        if not item in failed_rules:
            continue

        failed_index = tmp_row.index(item)
        tmp_holder = tmp_row[failed_index]
        tmp_row[failed_index] = tmp_row[index]
        tmp_row[index] = tmp_holder
        index = failed_index
        failed_rules.remove(item)

    return row

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
        needs_fixing = False
        tmp_row = row.copy()
        for index, _ in enumerate(row):
            while True:
                before = rule_map[tmp_row[index]]['before']

                intersection = set(before) & set(tmp_row[index + 1:])
                if bool(intersection):
                    needs_fixing = True
                    tmp_row = fix_row(intersection, tmp_row, index)
                    continue
                break

        if needs_fixing:
            accepted_updates.append(tmp_row)

    accepted_updates_number = 0
    for update in accepted_updates:
        middle_number = update[math.floor(len(update) / 2)]
        accepted_updates_number += int(middle_number)

    print(accepted_updates_number)