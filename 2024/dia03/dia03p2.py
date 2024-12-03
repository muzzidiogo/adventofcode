import re

def do_muls(data:str) -> int:
    patterns = [r"mul\(\d{1,3}[,]\d{1,3}\)", r"do\(\)", r"don't\(\)"]
    combined_pattern = "|".join(patterns)
    instructions = re.finditer(combined_pattern, data)
    
    sum = 0
    mul = True
    for instruction in instructions:
        if instruction.group() == "don't()":
            mul = False
            continue
        elif instruction.group() == "do()":
            mul = True
            continue
        elif mul == True:
            pair = list(map(int, re.findall(r"\d{1,3}[,]\d{1,3}", instruction.group())[0].split(',')))
            sum += pair[0]*pair[1]
    return sum

def main() -> None:
    with open('input.txt', 'rt') as file:
        mem_data = file.read()
    
    sum = do_muls(mem_data)
    print(sum)

if __name__ == '__main__':
    main()