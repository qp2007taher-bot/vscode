import password_checker
import data_converter
import ip_generator
import CAESAR_CIPHER


def main_menu():
    """
    Main execution loop and menu routing.
    """
    while True:
        print("\n\n" + "=" * 46 + "\n\n")
        print("        CYBERSECURITY MULTI-TOOL CLI")
        print("\n\n" + "=" * 46 + "\n\n")
        print("  [1] Password Strength Checker")
        print("  [2] Data & Number Converter")
        print("  [3] Local IP Address Generator")
        print("  [4] Encode and Decode text (CAESAR CIPHER)")
        print("  [0] Exit Program")
        print("\n\n" + "=" * 46 + "\n\n")

        user_choice = input("\n\nSelect an option (0-4): ").strip()
        print("\n")
        
        if user_choice == "1":
            password_checker.x()
        elif user_choice == "2":
            data_converter.x()
        elif user_choice == "3":
            ip_generator.x()
        elif user_choice == "4":
            CAESAR_CIPHER.x()
        elif user_choice == "0":
            break
        else:
            print("\n\n[Error404] Invalid selection. Please enter a number from 0 to 4.")


if __name__ == "__main__":
    main_menu()
