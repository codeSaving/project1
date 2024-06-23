def main():
    num_days = int(input('For how many days do you have sales: '))
    #open a new file named sale_text
    sales_file =  open('sales.text', 'w')
    for count in range(1, num_days+ 1):
        sales = float(input(f'Enter the sales for day #{count}: '))
        # write the sales amount to the file
        sales_file.write(f'{sales}\n')
        #close the file
        sales_file.close()
        print('Data written to sales.text.')
        #call the main function
main()
