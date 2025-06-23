import sys
from typing import Tuple, Callable

# ================================================================================
# CALCULATOR OPERATIONS
# ================================================================================

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

# ================================================================================
# INPUT/OUTPUT HANDLERS
# ================================================================================

def get_valid_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("❌ Invalid number! Try again.")
        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting.")
            sys.exit(0)

def get_operation_choice() -> Tuple[str, Callable[[float, float], float]]:
    operations = {
        '1': ('+', add, "Addition"),
        '2': ('-', subtract, "Subtraction"),
        '3': ('*', multiply, "Multiplication"),
        '4': ('/', divide, "Division")
    }

    while True:
        try:
            print("\n📋 SELECT OPERATION")
            print("-" * 30)
            for key, (_, _, name) in operations.items():
                print(f"{key}. {name}")
            print("0. Exit")
            print("-" * 30)

            choice = input("Enter your choice: ").strip()
            if choice == '0':
                return None, None
            elif choice in operations:
                symbol, func, _ = operations[choice]
                return symbol, func
            else:
                print("❌ Invalid choice! Select from 0–4.")
        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting.")
            sys.exit(0)

# ================================================================================
# DISPLAY
# ================================================================================

def display_calculation(x: float, operator: str, y: float, result: float):
    print("\n📊 Result:")
    print(f"{x} {operator} {y} = {result}")

def display_goodbye(calculations_done: int):
    print("\n" + "=" * 50)
    print("👋 Thanks for using the calculator.")
    print(f"🧮 Total calculations: {calculations_done}")
    print("✅ Developed by Nirnay")
    print("=" * 50)

# ================================================================================
# MAIN LOGIC
# ================================================================================

def main():
    calculations_done = 0
    print("=" * 50)
    print("🧮 Welcome to the CLI Calculator")
    print("=" * 50)

    while True:
        operator, operation_func = get_operation_choice()

        if not operator:
            break

        try:
            x = get_valid_number("Enter first number: ")
            y = get_valid_number("Enter second number: ")
            result = operation_func(x, y)
            display_calculation(x, operator, y, result)
            calculations_done += 1
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

        cont = input("\n🔁 Do another calculation? (y/n): ").strip().lower()
        if cont not in ('y', 'yes', ''):
            break

    display_goodbye(calculations_done)

if __name__ == "__main__":
    main()