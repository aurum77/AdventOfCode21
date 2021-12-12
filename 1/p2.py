def main():
    file = open("input.txt")
    lines = file.read().splitlines()
    counter = int(0)
    old = int(0)
    sums = list()

    for i in range(0, len(lines) - 2):
        # i = 0 | 0 1 2
        # i = 1 | 1 2 3
        # i = 2 | 2 3 4

        sums.append(int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]))

        old = int(sums[i])

    for i in range(1, len(sums)):

        if int(sums[i]) > old:
            counter += 1

        old = int(sums[i])

    print(sums)
    print(counter)

if __name__ == "__main__":
    main()