from typing import List, Tuple

def separate_lists(filepath: str) -> Tuple[List[int], List[int]]:
    """Separa as listas esquerda e direita de um arquivo de texto"""
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

def similarity_score(left: List[int], right:List[int]) -> int:
    """Calcula o Similarity Score: a soma de cada elemento de left 
    multiplicado pelo número de vezes que aparece em right."""
    return sum(numl * right.count(numl) for numl in left)

def main():
    file = 'input.txt'
    left, right = separate_lists(file)
    print(f'Similarity score: {similarity_score(left, right)}')

if __name__ == '__main__':
    main()