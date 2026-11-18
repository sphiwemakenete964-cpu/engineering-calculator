from ohms_law import ohms_law_calculator
from power_calculator import power_calculator


def main():
    while True:
        print("\n===== SPHIWE'S ENGINEERING TOOLKIT =====")
        print("1. Ohm's Law Calculator")
        print("2. Electrical Power Calculator")
        print("3. About this project")
        print("4. Exit")
        print("5. Voltage Divider Calculator")

        choice = input("Select an option: ")

        if choice == "1":
            ohms_law_calculator()

        elif choice == "2":
            power_calculator()

        elif choice == "3":
            print("\nAbout this project:")
            print("A Python toolkit for electrical calculations.")
            print("Created by Sphiwe.")

        elif choice == "4":
            print("Exiting Engineering Toolkit.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
