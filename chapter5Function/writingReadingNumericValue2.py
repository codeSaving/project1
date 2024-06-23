def main():
    infile = open('numbers.txt', 'r')

    # read 3 numbers from the file
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # close the file
    infile.close()

    # add the 3 numbers
    total = num1 + num2 + num3

    # display the numbers and their total
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'Their total is: {total}')


if __name__ == '__main__':
    main()


