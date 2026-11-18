def voltage_divider_calculator():
    print("\n=== Voltage Divider Calculator ===")

    try:
        vin = float(input("Enter input voltage (V): "))
        r1 = float(input("Enter R1 (Ohms): "))
        r2 = float(input("Enter R2 (Ohms): "))

        if r1 + r2 == 0:
            print("Error: Total resistance cannot be zero.")
        else:
            vout = vin * (r2 / (r1 + r2))
            print("Output voltage =", vout, "V")

    except ValueError:
        print("Error: Please enter numerical values.")


if __name__ == "__main__":
    voltage_divider_calculator()