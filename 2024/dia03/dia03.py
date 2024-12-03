import re

def do_muls(data:str) -> int:
    instructions = re.findall(r"mul\(\d{1,3}[,]\d{1,3}\)", data)
    
    sum = 0
    for mul in instructions:
        pair = list(map(int, re.findall(r"\d{1,3}[,]\d{1,3}", mul)[0].split(',')))
        sum += pair[0]*pair[1]

    return sum

def main() -> None:
    with open('input.txt', 'rt') as file:
        mem_data = file.read()
    
    sum = do_muls(mem_data)
    print(sum)

if __name__ == '__main__':
    main()