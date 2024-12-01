from typing import List, Tuple

def separate_lists(filepath: str) -> Tuple[List[int], List[int]]:
    left, right = [], []
    
    with open(filepath, 'rt') as file:
        for line in file:
            line.removesuffix('\n')
            separated_line = line.split('   ')
            left.append(separated_line[0])
            right.append(separated_line[1])
        
    left = sorted([int(num) for num in left])
    right = sorted([int(num) for num in right])
    
    return left, right

def find_distance(left: List[int], right:List[int]):
    dist = [abs(x - y) for x, y in zip(left, right)]
    return sum(dist)

def main():
    file = 'demo.txt'
    left, right = separate_lists(file)
    print(f'Sum of the distances: {find_distance(left, right)}')

if __name__ == '__main__':
    main()