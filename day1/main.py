def main():
    with open("day1\input.txt") as input:
        lines = input.readlines()
        lines = [line.strip() for line in lines]
        
        count = 0
        last = int(lines[0])
        for line in lines[1:]:
            if int(line) > last:
                count += 1
            last = int(line)
        
        print(count)

        groups = []
        for i in range(len(lines)):
            try:
                temp = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
                groups.append(temp)
            except:
                pass

        count = 0
        last = groups[0]
        for group in groups[1:]:
            if group > last:
                count += 1
            last = group
        print(count)

        

if __name__ == "__main__":
    main()