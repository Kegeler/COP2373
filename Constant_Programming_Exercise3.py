# Project Analyze expenses monthly


# Get expenses from the user
def get_expenses():
    num_expenses = int(input("How many expenses do you want to enter? "))
    expenses = []
    for i in range(num_expenses):
        expense_type = input(f"Enter the type of expense #{i+1}: ")
        amount = float(input(f"Enter the amount for {expense_type}: "))
        expenses.append([expense_type, amount])
    return expenses

# Function to analyze expenses (total, highest, lowest)
def analyze_expenses(expenses):
    total_expense = 0
    highest_expense = expenses[0]
    lowest_expense = expenses[0]

    for expense in expenses:
        # Calculate sum the amounts
        total_expense += expense[1]
        # Determine the highest
        if expense[1] > highest_expense[1]:
            highest_expense = expense
        # check for lowest
        if expense[1] < lowest_expense[1]:
            lowest_expense = expense

    return total_expense, highest_expense, lowest_expense

# Main program
def main():
    expenses = get_expenses()
    total, highest, lowest = analyze_expenses(expenses)
    print("\nExpense Summary:")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

# Run the program
if __name__ == "__main__":
    main()