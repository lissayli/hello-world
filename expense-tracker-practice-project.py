```python
# EXPENSE TRACKER PRACTICE PROJECT
# 31-DEC-2026
# PROJECT 1

#Initial Settings
expenseList = []

#Title
print("Welcome to the Daily Expense Tracker!")
print("")

#Display Menu
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

#Interactivity
while True:
    choice = int(input())
    if choice == 1:                   #1. Add a new expense
        expense = float(input())
        expenseList.append(expense)
        print("Expense added successfully!")
    if choice == 2:                   #2. View all expenses
        if not expenseList:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, item in enumerate(expenseList, start=1):
                print(f"{index}. {item}")
   if choice == 3:                    #3. Calc ttl & av expenses
        if not expenseList:
            print("No expenses recorded yet.")
        else:
            totalExpenses = float(sum(expenseList))
            averageExpenses = float(sum(expenseList) / len(expenseList))                    #THIS IS NOT A NEW LINE
            print(f"Total expense: {totalExpenses}")
            print(f"Average expense: {averageExpenses}")
    if choice == 4:                  #4. Clear expenses
        expenseList.clear()
        print("All expenses cleared.")
    if choice == 5:                   #5. Exit
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    if choice > 5:
        print("Invalid choice. Please try again.")
    if choice < 1:
        print("Invalid choice. Please try again.")
```
