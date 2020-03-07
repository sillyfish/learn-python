def loop(index, step):
    numbers = []

    # while loop
    # i = 0
    # while i < index:
    #     numbers.append(i)
    #     i += step

    # for loop
    for i in range(0, index, step):
        numbers.append(i)

    print("The numbers: ")

    for num in numbers:
        print(num, end=', ')

    print("")
