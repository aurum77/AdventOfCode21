def main():
    file = open("input.txt", "r")
    lines = file.read().splitlines()
    depth = int(0)
    horizontal = int(0)

    for line in lines:
        # i could've done just a single variable
        # and used the indexes to read the magnitude
        # and the direction but it's more idiomatic this way 
        direction = line.split(" ")[0]
        magnitude = int(line.split(" ")[1])
        if direction == "forward":
            horizontal += magnitude

        elif direction == "up":
            depth -= magnitude

        elif direction == "down":
            depth += magnitude

    print(f'{horizontal} {depth}')
    print(f'result: {horizontal * depth}')

            

if __name__ == "__main__":
    main()