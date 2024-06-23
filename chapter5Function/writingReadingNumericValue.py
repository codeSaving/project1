def main():
    outfile = open('numbers.txt', 'w')

    # get 3 numbers from the user
    num1 = input('Enter a number: ')
    num2 = input('Enter another number: ')
    num3 = input('Enter another number: ')

    # write 3 numbers to a file
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # close the file
    outfile.close()

    print('Data written to numbers.txt')


main()


