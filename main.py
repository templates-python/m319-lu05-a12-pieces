def main():
    print('Give numbers:')
    number = 0
    sums = 1      # To compensate for -1 for terminating
    counter = -1  # We start with -1 to compensate for last iteration
    odd = 0
    even = 0
    while number != -1:
        number = int(input(''))
        if (number % 2 == 0 and number != -1):
            even += 1
        if (number % 2 == 1 and number != -1):
            odd += 1
        sums += number
        counter += 1
    print('Thx! Bye!')
    print(f'Sum: {sums}')
    print(f'Numbers: {counter}')
    average = sums / counter
    print(f'Average: {average}')
    print(f'Even: {even}')
    print(f'Odd: {odd}')


if __name__ == '__main__':
    main()
