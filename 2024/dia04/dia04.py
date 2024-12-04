from typing import List

pattern = 'XMAS'
directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (-1,-1), (1,-1)]

def find_xmas(matrix:List) -> int:
    count = 0
    size = len(matrix)

    def match(i, j, di, dj):
        for k in range(4):
            ni, nj = i+k*di, j+k*dj
            if not(0 <= ni < size and 0 <= nj < size) or matrix[ni][nj] != pattern[k]:
                return False
        return True

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'X' or matrix[i][j] == 'S':
                for di, dj in directions:
                    if match(i, j, di, dj):
                        count += 1
    return count

def main() -> None:
    input_matrix = []
    with open('input.txt', 'rt') as file:
        for line in file:
            input_matrix.append(line.strip('\n'))
    
    print(find_xmas(input_matrix))

if __name__ == '__main__':
    main()
