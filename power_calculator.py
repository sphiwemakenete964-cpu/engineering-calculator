print("=== Electrical Power Calculator ===")
print("1. Calculate power using voltage and current")
print("2. Calculate power using current and resistance")
print("3. Calculate power using voltage and resistance")

choice = input("Choose an option: ")

if choice == "1":
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    power = voltage * current

    print("Power =", power, "W")

elif choice == "2":
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ohms): "))

    power = current ** 2 * resistance

    print("Power =", power, "W")

elif choice == "3":
    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (Ohms): "))

    power = voltage ** 2 / resistance

    print("Power =", power, "W")

else:
    print("Invalid option")
