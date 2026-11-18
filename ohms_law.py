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

            voltage = current * resistance
            print("Voltage =", voltage, "V")

        elif choice == "2":
            voltage = float(input("Enter voltage (V): "))
            resistance = float(input("Enter resistance (Ohms): "))

            if resistance == 0:
                print("Error: Resistance cannot be zero.")
            else:
                current = voltage / resistance
                print("Current =", current, "A")

        elif choice == "3":
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))

            if current == 0:
                print("Error: Current cannot be zero.")
            else:
                resistance = voltage / current
                print("Resistance =", resistance, "Ohms")

        else:
            print("Invalid option.")

    except ValueError:
        print("Error: Please enter numerical values.")


if __name__ == "__main__":
    ohms_law_calculator()
