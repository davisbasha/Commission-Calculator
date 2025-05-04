#Create a variable to control the loop
keep_going = 'y'
#Calculate a series of commission
while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    #Calculate the commission
    commission = sales = comm_rate
    #Display commission
    print(f'The commission is ${commission:,.2f}')
#Lets check and see if the user wants to calculate more commission
keep_going = input('Do you want to calculate another commission' + 'commission (enter y for yes): ')