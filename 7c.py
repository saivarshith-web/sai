def numbers_between_1000_and_2000():
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            print(num, end=" ")
numbers_between_1000_and_2000()
