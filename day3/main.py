def main():
    with open("day3\input.txt") as input:
        lines = input.readlines()
        lines = [line.strip() for line in lines]
        
        gamma = ""
        epsilon =""

        for i in range(len(lines[0])):
            ones = 0
            zeros = 0
            for line in lines:
                if line[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones > zeros:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
    decimalGamma = binaryToDecimal(gamma)
    decimalEpsilon = binaryToDecimal(epsilon)

    print(f"result part 1: {decimalGamma * decimalEpsilon}")

def binaryToDecimal(binaryString):
    temp = 0
    power = 0
    for i in range(len(binaryString), 0, -1):
        current = int(binaryString[i-1])
        if(current == 1):
            temp += pow(2, power)
        power += 1
    return temp
    
if __name__ == "__main__":
    main()