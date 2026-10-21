"""
Converts storage sizes and converts decimal numbers to Binary/Hexadecimal.
"""

def x():
    print("\n\n" + "-" * 46 + "\n\n")
    print("         [2] DATA & NUMBER CONVERTER")
    print("\n\n" + "-" * 46 + "\n\n")
    print("\n\nSelect conversion type:\n\n")
    print("  [A] Storage Size Converter (MB)")
    print("  [B] Number System Converter (Decimal -> Bin / Hex)\n\n")

    choice = input("\n\nYour choice (A/B): ").strip().upper()
    print("\n\n\n\n" + "-" * 46 + "\n\n")

    if choice == "A":
        try:
            mb = float(input("\n\nEnter size in Megabytes (MB): "))

            bytes_val = mb * 1024 * 1024
            kb_val = mb * 1024
            gb_val = mb / 1024

            print("\n\n--- Conversion Results ---\n\n")
            print(f"  • Bytes:       {bytes_val} B")
            print(f"  • Kilobytes:   {kb_val} KB")
            print(f"  • Gigabytes:   {gb_val} GB")
            print("\n\n")
        except ValueError:
            print("\n\n[!] Invalid input. Please enter a valid number.")

    elif choice == "B":
        try:
            num = int(input("\n\nEnter a decimal number: "))

            print("\n\n--- Conversion Results ---\n\n")
            print(f"  • Binary:      {bin(num)}")
            print(f"  • Hexadecimal: {hex(num)}")
            print(f"  • Octal:       {oct(num)}")

        except ValueError:
            print("\n\n[!] Invalid input. Please enter a valid integer.")

    else:
        print("\n\n[!] Invalid option selected.")

if __name__ == "__main__":
    x()
