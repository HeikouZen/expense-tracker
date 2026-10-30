# Expense Tracker - Installment 5
# Author: Baruelo Rafael M.
# A simple program for tracking and managing expenses.

name: str = ""
budget: float = 0.0
tax_percent: float = 0.0
subtotal: float = 0.0
count: int = 0
choice: str = ""

amount: float = 0.0
tax: float = 0.0
total: float = 0.0
left: float = 0.0
over_budget: bool = False


print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("\t\tInstallment 5")
print("=" * 40)


name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

print("\nMAIN MENU")
print("\t[1] Add an expense")
print("\t[2] View all expenses (coming soon)")
print("\t[3] Show total spent")
print("\t[4] Exit")


while True:
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))

        subtotal = subtotal + amount
        count = count + 1

        if amount > 200:
            print("\tHuge expense - are you sure?")
        elif amount > 100:
            print("\tBig expense.")
        elif amount > 50:
            print("\tModerate expense.")
        else:
            print("\tSmall expense.")

    elif choice == "2":
        print("Coming soon! the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total

        over_budget = total > budget

        print("\tExpenses:\t", count)
        print(f"\tSubtotal:\t${subtotal:.1f}")
        print(f"\tTax ({tax_percent:.1f}%):\t${tax:.1f}")
        print(f"\tGrand total:\t${total:.1f}")

        if over_budget:
            print(f"\tOver budget by ${total - budget:.1f}!")

        elif total > budget * 0.90:
            print(f"\tCareful: only ${left:.1f} left.")

        else:
            print(f"\tWithin budget. ${left:.1f} left.")

        print("-" * 40)
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Baruelo Rafael\t|\tInstallment 5")
        print("=" * 40)

        break
    else:
        print("Please choose 1, 2, 3 or 4.")
