def main():
    file = open("input.txt", "r")
    lines = file.read().splitlines()
    counter = int(0)
    old = int(0)

    for i in range(1, len(lines)):

        if int(lines[i]) > old:
            counter += 1

        old = int(lines[i])

    print(counter)

if __name__ == "__main__":
    main()