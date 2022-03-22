def main():
    with open("day2\input.txt") as input:
        lines = input.readlines()
        lines = [line.strip() for line in lines]
        
        splitLines = []
        for line in lines:
            temp = line.split()
            splitLines.append(temp)
        
        part2(splitLines)
        horizontal = 0
        depth = 0
        for line in splitLines:
            match line[0]:
                case 'forward':
                    horizontal += int(line[1])
                case 'down':
                    depth += int(line[1])
                case 'up':
                    depth -= int(line[1])
                case _:
                    print("no")
        print(f"horizontal: {horizontal}")
        print(f"depth: {depth}")
        print(f"part 1 result: {horizontal * depth}")

def part2(lines):
    horizontal = 0
    depth = 0
    aim = 0
    print(f"lines{lines}")
    for line in lines:
        match line[0]:
            case 'forward':
                horizontal += int(line[1])
                depth += aim * int(line[1])
            case 'down':
                aim += int(line[1])
            case 'up':
                aim -= int(line[1])
    print(f"horizontal: {horizontal}")
    print(f"depth: {depth}")
    print(f"part 2 result: {horizontal * depth}")
    
if __name__ == "__main__":
    main()