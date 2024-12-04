from typing import List

pattern = 'MS'
directions = [(1,1), (-1,1)]

def find_xmas(matrix:List) -> int:
    count = 0
    size = len(matrix)

    def match(i, j, di, dj):
        if 0 <= i + di < size and 0 <= j + dj < size and \
           0 <= i - di < size and 0 <= j - dj < size:
            if matrix[i+di][j+dj] in pattern and \
               matrix[i-di][j-dj] in pattern and \
               matrix[i-di][j-dj] != matrix[i+di][j+dj]:
                return True
            return False

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'A':
                for di, dj in directions:
                    if not match(i, j, di, dj):
                        break
                else: count += 1
                
    return count

def main() -> None:
    input_matrix = []
    with open('input.txt', 'rt') as file:
        for line in file:
            input_matrix.append(line.strip('\n'))
    
    print(find_xmas(input_matrix))

if __name__ == '__main__':
    main()