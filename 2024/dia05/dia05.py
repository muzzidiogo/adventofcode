from typing import List
from math import floor

def check_updates(rules:List[List[int]], updates:List[List[int]]) -> List[List[int]]:
    correctUpdates = []
    for update in updates:
        for rule in rules:
            if rule[0] in update and rule [1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    break
        else: 
            print(update)
            correctUpdates.append(update[floor(len(update)/2)])
    
    print('---')
    return sum(correctUpdates)

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
    input_path = 'demo.txt'
    rules, updates = get_input(input_path)
    print(check_updates(rules, updates))
    
if __name__ == '__main__':
    main()