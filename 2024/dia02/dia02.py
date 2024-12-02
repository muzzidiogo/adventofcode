from typing import List

def get_reports(filepath: str) -> List[List[int]]:
    """Separa as listas esquerda e direita de um arquivo de texto"""
    reports = []
    
    with open(filepath, 'rt') as file:
        for report in file:
            report = report.removesuffix('\n')
            levels = report.split(' ')
            reports.append([int(num) for num in levels])
    
    return reports

def all_increasing_or_decreasing(report:List[int]) -> bool:
    """Confere se os níveis de cada report crescem ou decrescem consistentemente"""

    is_increasing = True
    is_decreasing = True
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if diff < 0:
            is_increasing = False
        elif diff > 0:
            is_decreasing = False
        elif diff == 0:
            is_decreasing = False
            is_increasing = False
    
    return is_decreasing or is_increasing

def diff_in_range(report:List[int]) -> bool:
    """Confere se a diferença entre os níveis está entre 1 e 3"""

    in_range = True
    for i in range(len(report)-1):
        diff = abs(report[i+1] - report[i])
        if diff < 1 or diff > 3:
            in_range = False
    
    return in_range

def main() -> None:
    """Função de Execução do Código"""

    filepath = 'input.txt'
    reports = get_reports(filepath)

    safe = 0
    for report in reports:
        if diff_in_range(report) and all_increasing_or_decreasing(report):
            safe += 1
    
    print(f'Total of {safe} safe reports')

if __name__ == '__main__':
    main()