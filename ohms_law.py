def calculate_voltage(current, resistance):
    return current * resistance


def calculate_current(voltage, resistance):
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance


def calculate_resistance(voltage, current):
    if current == 0:
        raise ValueError("Current cannot be zero.")
    return voltage / current

def ohms_law_calculator():
    print("\n=== Ohm's Law Calculator ===")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")

    choice = input("Choose an option: ")

    try:
        if choice == "1":
            current = float(input("Enter current (A): "))
            resistance = float(input("Enter resistance (Ohms): "))

            voltage = calculate_voltage(current, resistance)
            print("Voltage =", voltage, "V")

        elif choice == "2":
            voltage = float(input("Enter voltage (V): "))
            resistance = float(input("Enter resistance (Ohms): "))

            current = calculate_current(voltage, resistance)
            print("Current =", current, "A")

        elif choice == "3":
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))

            resistance = calculate_resistance(voltage, current)
            print("Resistance =", resistance, "Ohms")

        else:
            print("Invalid option.")

    except ValueError:
        print("Error: Please enter numerical values.")


if __name__ == "__main__":
    ohms_law_calculator()
