from typing import List 
from math import floor

def check_rules(rules: List[List[int]], update: List[int]):
    changed = False
    for rule in rules:
        if rule[0] in update and rule [1] in update:
            i, j = update.index(rule[0]), update.index(rule[1])
            if i > j:
                temp1 = update[i]
                temp2 = update[j] 
                update[i] = temp2
                update[j] = temp1
                changed = True
    return update, changed

def check_updates(rules:List[List[int]], updates:List[List[int]]) -> List[List[int]]:
    incorrectUpdates = []
    for update in updates:
        incorrect = False
        for rule in rules:
            if rule[0] in update and rule [1] in update:
                i, j = update.index(rule[0]), update.index(rule[1])
                if i > j:
                    temp1 = update[i]
                    temp2 = update[j] 
                    update[i] = temp2
                    update[j] = temp1
                    incorrect = True
        if incorrect:
            changed = False
            new, changed = check_rules(rules, update)
            while changed:
                update = new
                new, changed = check_rules(rules, update)
            incorrectUpdates.append(update)

    return incorrectUpdates

def get_input(filepath:str) -> tuple[List[List[int]], List[List[int]]]:
    rules, updates = [], []
    flag = True
    with open(filepath, 'rt') as file:
        for line in file:
            if line == '\n':
                flag = False
                continue
            if flag:
                rules.append(line.removesuffix('\n'))
            else:
                updates.append(line.removesuffix('\n'))
    
    rules = [list(map(int, rule.split('|'))) for rule in rules]
    updates = [list(map(int, update.split(','))) for update in updates]

    return rules, updates

def main() -> None:
    # [floor(len(update)/2)]
    input_path = 'input.txt'
    rules, updates = get_input(input_path)
    incorrectUpdates = check_updates(rules, updates)
    print(incorrectUpdates)
    
    center = []
    for update in incorrectUpdates:
        center.append(update[floor(len(update)/2)])
    
    print(sum(center))
    
if __name__ == '__main__':
    main()