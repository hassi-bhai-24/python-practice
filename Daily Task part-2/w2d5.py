FILE = "expenses.txt"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    with open(FILE, "a") as f:
        f.write(amount + "," + category + "\n")
    print("Expense added!\n")


def view_expenses():
    try:
        with open(FILE, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("No expenses found.\n")
        return

    print("\n--- All Expenses ---")
    for line in data:
        amount, category = line.strip().split(",")
        print(amount, "-", category)
    print()


def summary_by_category():
    try:
        with open(FILE, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("No expenses found.\n")
        return

    summary = {}

    for line in data:
        amount, category = line.strip().split(",")
        amount = float(amount)
        if category not in summary:
            summary[category] = amount
        else:
            summary[category] += amount

    print("\n--- Category Summary ---")
    for cat in summary:
        print(cat + ":", summary[cat])
    print()


def main():
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            break
        else:
            print("Invalid option!\n")


main()
