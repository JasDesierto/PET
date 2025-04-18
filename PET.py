

#Initialization

finances = {}

#Defining Function

def get_expense():
    try:
        month = input("Please provide the current month (eg. January, February or December): ")
        expense = float(input(f"Please provide your expenses for the month of {month}: "))
        return month,expense

    except ValueError:
        print("Please provide the correct value")
        return None,None


# Main loop   
while True:

    print("1.) Add Expense")
    print("2.) Summary")
    print("3.) Exit")

    # Requesting for user input

    try:
        choice = int(input("Please provide your choice (1-3): "))

    except ValueError:
        print("Please enter a valid choice (1-3)")
        continue

    if choice == 1:
         month, expense = get_expense() # Calls the function get_expense()
         if month is not None and expense is not None:  # This is to ensure valid input, if valid, the nested if - else statement will commence.
            if month in finances:
                finances [month] +=expense # To Add more expenses to the existing key:value in the dictionary.
                print(f"Your expense of {expense} has been recorded for the month of {month}")

            else:
                finances[month] = expense # If not in dict, adds the new month to the dictionary.
                print(f"Your expense of {expense} for {month} been recorded, thank you.")

    elif choice == 2:
        for month,expense in finances.items():
            print(f"{month} -- {expense:,.2f}")
        total = sum (finances.values())
        print("~~~~~~~~~~~~~~~~~~~~~")
        print()
        print (f"Your total expenses is: {total:,.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~")


    elif choice == 3:
        print ("Thank you.")
        break

    else:
        print("Invalid Choice. Please enter 1 or 2.")














