# Expense Tracker - Installment 2
# Author: Baruelo Rafael M.
# A simple program for tracking and managing expenses.

name : str = ""
item1 : str = ""
amount1 : float = 0.0

item2 : str = ""
amount2 : float = 0.0

total : float = 0.0
average : float = 0.0

print("=" * 40)
print("            EXPENSE TRACKER                  ")
print("        Know where your money goes.          ")
print("=" * 40)

print("\nMAIN MENU")
print(" [1] Add an expense            (coming soon)")
print(" [2] View all expenses         (coming soon)")
print(" [3] Show total spent          (coming soon)")
print(" [4] Exit                      (coming soon)")

name = input("\nWhat's your name?: ")
print(f"\nWelcome, {name}! Let's log two expenses.")

item1 = input("\nFirst expense?: ")
amount1 = float(input("Amount?: "))

item2 = input("\nSecond expense?: ")
amount2 = float(input("Amount?: "))

total = amount1 + amount2
average = total / 2

print(" ")
print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t ${amount1:.1f}")
print(f" - {item2}:\t ${amount2:.1f}")
print(f" - Total Spent:\t ${total:.1f}")
print(f" - Average:\t ${average:.1f}")
print("-" * 40)
print("Made by: Baruelo Rafael  |  Installment 2")