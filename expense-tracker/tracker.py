# Expense Tracker - Installment 4
# Author: Baruelo Rafael M.
# A simple program for tracking and managing expenses.

name : str = ""
item1 : str = ""
amount1 : float = 0.0

item2 : str = ""
amount2 : float = 0.0

total : float = 0.0
average : float = 0.0

subtotal: float = 0.0
average: float = 0.0
tax_percent: float = 0.0
tax: float = 0.0
total: float = 0.0
budget: float = 0.0
over_budget: bool = False
left: float = 0.0


print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("MAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"\nWelcome, {name}! Let's log two expenses.")

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))

if amount1 > 200:
    print("\tHuge expense - are you sure?")
elif amount1 > 100:
    print("\tBig expense.")
elif amount1 > 50:
    print("\tModerate expense.")
else:
    print("\tSmall expense.")

item2 = input("\nSecond expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("\tHuge expense - are you sure?")
elif amount2 > 100:
    print("\tBig expense.")
elif amount2 > 50:
    print("\tModerate expense.")
else:
    print("\tSmall expense.")

subtotal = amount1 + amount2

if amount1 > 100 and amount2 > 100:
    print("\tTwo big expenses in a row - slow down!")

average = subtotal / 2

tax_percent = float(input("\nTax rate%? "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("\n", "-" * 40)
print("SUMMARY")
print(f"- {item1}:\t${amount1:.1f}")
print(f"- {item2}:\t${amount2:.1f}")
print(f"Subtotal:\t${subtotal:.1f}")
print(f"Average:\t${average:.2f}")
print(f"Tax ({tax_percent:.1f}%):\t${tax:.1f}")
print(f"Grand total:\t${total:.1f}")

if over_budget:
    print(f"Over budget by ${total - budget:.1f}!")
elif total > budget * 0.90:
    print(f"Careful: only ${left:.1f} left.")
else:
    print(f"Within budget. ${left:.1f} left.")

print("-" * 40)
print("Made by: Baruelo Rafael\t|\tInstallment 4")
