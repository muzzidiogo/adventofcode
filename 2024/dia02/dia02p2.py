from typing import List

def get_reports(filepath: str) -> List[List[int]]:
    """Separa as listas esquerda e direita de um arquivo de texto"""
    
    reports = []
    with open(filepath, 'rt') as file:
        for report in file:
            levels = report.removesuffix('\n').split(' ')
            reports.append([int(num) for num in levels])
    
    return reports

def is_safe(report:List[int]) -> bool:
    """Confere se o report é seguro"""

    is_increasing = True
    is_decreasing = True
    in_range = True

    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if abs(diff) < 1 or abs(diff) > 3:
            in_range = False
        if diff < 0:
            is_increasing = False
        elif diff > 0:
            is_decreasing = False
        elif diff == 0:
            is_decreasing = False
            is_increasing = False
    
    return (is_decreasing or is_increasing) and in_range
    
def main() -> None:
    """Função de Execução do Código"""

    filepath = 'input.txt'
    reports = get_reports(filepath)

    safe = 0
    for report in reports:
        if any(is_safe(report[:n]+report[n+1:]) for n in range(len(report))):
            safe += 1
    
    print(f'Total of {safe} safe reports')

if __name__ == '__main__':
    main()