def calculate_power_vi(voltage, current):
    return voltage * current


def calculate_power_ir(current, resistance):
    return current ** 2 * resistance


def calculate_power_vr(voltage, resistance):
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage ** 2 / resistance

def power_calculator():
    print("\n=== Electrical Power Calculator ===")
    print("1. Calculate power using voltage and current")
    print("2. Calculate power using current and resistance")
    print("3. Calculate power using voltage and resistance")

    choice = input("Choose an option: ")

    try:
        if choice == "1":
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))

            power = calculate_power_vi(voltage, current)
            print("Power =", power, "W")

        elif choice == "2":
            current = float(input("Enter current (A): "))
            resistance = float(input("Enter resistance (Ohms): "))

            power = calculate_power_ir(current, resistance)
            print("Power =", power, "W")

        elif choice == "3":
            voltage = float(input("Enter voltage (V): "))
            resistance = float(input("Enter resistance (Ohms): "))

            power = calculate_power_vr(voltage, resistance)
            print("Power =", power, "W")

        else:
            print("Invalid option.")

    except ValueError:
        print("Error: Please enter numerical values.")


if __name__ == "__main__":
    power_calculator()
