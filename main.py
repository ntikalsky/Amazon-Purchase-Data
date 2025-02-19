import pandas as pd
import data
import calculations

# open csv file
df = data.open_csv()

# clean data in csv file
df = data.data_clean(df)

print("Select desired operation.")
print("1. Total Spent")
print("2. Average Spent per Order")
print("3. Total Sales Tax Spent")
print("4. Largest Order")
print("5. Smallest Order")

while True:
    # get input from user
    choice = input("Enter number: ")

    # check if choice is one of the five options
    if choice in ('1', '2', '3', '4', '5'):

        if choice == '1':
            total = calculations.total_spent(df)
            print("Total Spent:", total)

        elif choice == '2':
            average = calculations.average_spent(df)
            print("Average Spent:", average)

        elif choice == '3':
            tax = calculations.sales_tax(df)
            print("Sales Tax Spent:", tax)

        elif choice == '4':
            large = calculations.largest_order(df)
            print("Largest Order:", large)

        elif choice == '5':
            small = calculations.smallest_order(df)
            print("Smallest Order:", small)
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do another calculation? (y/n): ")
        if next_calculation == "n":
          break
            
    # if input isn't one of the five options, print error
    else:
        print("Invalid Input")