#!/usr/bin/env python3
"""
Cybersecurity Multi-Tool CLI - Version 3.3 (Spacious & Clean UI)
Combines Password Strength Checker, Data Converter, IP Generator, 
Caesar Cipher, and Linux System Cache Cleaner into a single professional program.
"""

import os
import shutil
import subprocess
import sys

# Terminal Colors & Styles
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Constant Width for Long Separator Lines
WIDTH = 64

def clear_screen():
    """Clear terminal screen for a clean view."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner(title, subtitle=None, color=Colors.GREEN, border="="):
    """Prints a long separator line with a perfectly centered title and generous breathing room."""
    line = border * WIDTH
    # فراغات إضافية (أسطر فارغة) قبل وبعد العنوان لكي يأخذ راحته ولا يبدو مكدساً
    print(f"\n\n\n{Colors.CYAN}{line}{Colors.ENDC}")
    
    # Center title
    t_pad = (WIDTH - len(title)) // 2
    print(f"{Colors.BOLD}{color}{' ' * max(0, t_pad)}{title}{Colors.ENDC}")
    
    # Center subtitle if exists
    if subtitle:
        s_pad = (WIDTH - len(subtitle)) // 2
        print(f"{Colors.CYAN}{' ' * max(0, s_pad)}{subtitle}{Colors.ENDC}")
        
    print(f"{Colors.CYAN}{line}{Colors.ENDC}\n\n")


def password_checker():
    print_banner("[1] PASSWORD STRENGTH CHECKER", color=Colors.GREEN, border="-")

    password = input(f"{Colors.BOLD}Enter a password to analyze: {Colors.ENDC}")

    score = 0
    feedback = []

    # 1. Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # 2. Check for numeric digits
    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        score += 1
    else:
        feedback.append("Password lacks numeric characters (0-9).")

    # 3. Check for special symbols
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_symbol = any(char in symbols for char in password)
    if has_symbol:
        score += 1
    else:
        feedback.append("Password lacks special symbols (e.g., @, #, $).")

    # Display evaluation results
    print(f"\n\n{Colors.BLUE}--- Evaluation Summary ---{Colors.ENDC}\n")

    if score == 3:
        print(f"Result: {Colors.GREEN}{Colors.BOLD}STRONG (Passes security standards){Colors.ENDC}\n")
    elif score == 2:
        print(f"Result: {Colors.WARNING}{Colors.BOLD}MODERATE (Needs improvement){Colors.ENDC}\n")
    else:
        print(f"Result: {Colors.FAIL}{Colors.BOLD}WEAK (High security risk){Colors.ENDC}\n")

    if feedback:
        print(f"{Colors.WARNING}Recommendations:{Colors.ENDC}")
        for note in feedback:
            print(f"  • {note}")
        print()
        
    input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.ENDC}")


def data_converter():
    print_banner("[2] DATA & NUMBER CONVERTER", color=Colors.GREEN, border="-")
    
    print("Select conversion type:")
    print(f"  {Colors.BOLD}[A]{Colors.ENDC} Storage Size Converter (MB)")
    print(f"  {Colors.BOLD}[B]{Colors.ENDC} Number System Converter (Decimal -> Bin / Hex / Oct)\n")

    choice = input(f"{Colors.BOLD}Your choice (A/B): {Colors.ENDC}").strip().upper()
    print(f"\n{Colors.CYAN}{'-' * WIDTH}{Colors.ENDC}\n")

    if choice == "A":
        try:
            mb = float(input("Enter size in Megabytes (MB): "))
            bytes_val = mb * 1024 * 1024
            kb_val = mb * 1024
            gb_val = mb / 1024

            print(f"\n\n{Colors.BLUE}--- Conversion Results ---{Colors.ENDC}\n")
            print(f"  • Bytes:        {Colors.GREEN}{bytes_val:,.2f} B{Colors.ENDC}")
            print(f"  • Kilobytes:    {Colors.GREEN}{kb_val:,.2f} KB{Colors.ENDC}")
            print(f"  • Gigabytes:    {Colors.GREEN}{gb_val:,.4f} GB{Colors.ENDC}\n")
        except ValueError:
            print(f"\n{Colors.FAIL}[!] Invalid input. Please enter a valid number.{Colors.ENDC}")

    elif choice == "B":
        try:
            num = int(input("Enter a decimal number: "))
            print(f"\n\n{Colors.BLUE}--- Conversion Results ---{Colors.ENDC}\n")
            print(f"  • Binary:       {Colors.GREEN}{bin(num)}{Colors.ENDC}")
            print(f"  • Hexadecimal:  {Colors.GREEN}{hex(num)}{Colors.ENDC}")
            print(f"  • Octal:        {Colors.GREEN}{oct(num)}{Colors.ENDC}\n")
        except ValueError:
            print(f"\n{Colors.FAIL}[!] Invalid input. Please enter a valid integer.{Colors.ENDC}")

    else:
        print(f"\n{Colors.FAIL}[!] Invalid option selected.{Colors.ENDC}")
    
    input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.ENDC}")


def ip_generator():
    print_banner("[3] LOCAL IP ADDRESS GENERATOR", color=Colors.GREEN, border="-")

    subnet = input("Enter network prefix (Example: 192.168.1): ").strip()

    try:
        start_host = int(input("Enter start host (Example: 1): "))
        end_host = int(input("Enter end host (Example: 10): "))

        if start_host > end_host:
            print(f"\n{Colors.FAIL}[!] Start host cannot be greater than end host.{Colors.ENDC}")
            return
        
        if not (0 <= start_host <= 255 and 0 <= end_host <= 255):
            print(f"\n{Colors.FAIL}[!] Host values must be between 0 and 255.{Colors.ENDC}")
            return
        
        print(f"\n\n{Colors.BLUE}--- Generated Target IP Addresses ---{Colors.ENDC}\n")
        ip_list = []
        for host in range(start_host, end_host + 1):
            ip = f"{subnet}.{host}"
            ip_list.append(ip)
            print(f"  • {Colors.GREEN}{ip}{Colors.ENDC}")
        
        print(f"\n{Colors.BOLD}Successfully generated {len(ip_list)} IP addresses.{Colors.ENDC}\n")
        
    except ValueError:
        print(f"\n{Colors.FAIL}[!] Host boundaries must be valid integers.{Colors.ENDC}")

    input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.ENDC}")


def encode_caesar():
    print_banner("[4-1] ENCODE TEXT (CAESAR CIPHER)", color=Colors.GREEN, border="-")
    
    text = input('Enter text to encode: ')
    
    while True:    
        try:
            shift = int(input('Enter shift value (Example: 3): '))
            break
        except ValueError:
            print(f'{Colors.FAIL}[!] Invalid shift value. Please enter an integer.{Colors.ENDC}')
    
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char)

    encrypted_text = ''.join(result)
    print(f"\n\n{Colors.BLUE}--- Encrypted Result ---{Colors.ENDC}\n")
    print(f"  Ciphertext: {Colors.GREEN}{Colors.BOLD}{encrypted_text}{Colors.ENDC}\n")
    input(f"\n{Colors.CYAN}Press Enter to return...{Colors.ENDC}")


def decode_caesar():
    print_banner("[4-2] DECODE TEXT (CAESAR CIPHER)", color=Colors.GREEN, border="-")
    
    text = input('Enter text to decode: ')

    while True:
        try:
            shift = int(input('Enter shift value (Example: 3): '))
            break
        except ValueError:
            print(f'{Colors.FAIL}[!] Invalid shift value. Please enter an integer.{Colors.ENDC}')

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char)

    decrypted_text = ''.join(result)
    print(f"\n\n{Colors.BLUE}--- Decrypted Result ---{Colors.ENDC}\n")
    print(f"  Plaintext: {Colors.GREEN}{Colors.BOLD}{decrypted_text}{Colors.ENDC}\n")
    input(f"\n{Colors.CYAN}Press Enter to return...{Colors.ENDC}")


def caesar_cipher_menu():
    while True:
        print_banner("CAESAR CIPHER TOOLKIT", color=Colors.GREEN, border="-")
        print(f"  {Colors.BOLD}[1]{Colors.ENDC} Encode Text")
        print(f"  {Colors.BOLD}[2]{Colors.ENDC} Decode Text")
        print(f"  {Colors.BOLD}[0]{Colors.ENDC} Back to Main Menu")
        print(f"\n{Colors.CYAN}{'-' * WIDTH}{Colors.ENDC}")

        user_choice = input(f"\nSelect an option (0-2): ").strip()
        
        if user_choice == "1":
            encode_caesar()
        elif user_choice == "2":
            decode_caesar()
        elif user_choice == "0":
            break
        else:
            print(f"\n{Colors.FAIL}[!] Invalid selection. Please enter 0, 1, or 2.{Colors.ENDC}")


def system_cleaner():
    print_banner("[5] SYSTEM CACHE & FILE CLEANER", color=Colors.FAIL, border="=")
    
    confirm = input(f"{Colors.WARNING}Are you sure you want to clean system caches and temp files? (y/N): {Colors.ENDC}").strip().lower()
    if confirm != 'y':
        print(f"\n{Colors.BLUE}[!] Operation cancelled.{Colors.ENDC}\n")
        return

    print(f"\n\n{Colors.CYAN}{'=' * WIDTH}{Colors.ENDC}")
    print(f"{Colors.BOLD}{' ' * 17}=== Cleaning System Files ===     {Colors.ENDC}")
    print(f"{Colors.CYAN}{'=' * WIDTH}{Colors.ENDC}\n")

    print(f"{Colors.BLUE}[1/4]{Colors.ENDC} Cleaning user cache and temporary files...")
    cache_dir = os.path.expanduser("~/.cache")
    if os.path.exists(cache_dir):
        for item in os.listdir(cache_dir):
            item_path = os.path.join(cache_dir, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception:
                pass

    print(f"{Colors.BLUE}[2/4]{Colors.ENDC} Cleaning system packages and remnants (APT)...")
    try:
        subprocess.run(["sudo", "apt-get", "clean"], check=False)
        subprocess.run(["sudo", "apt-get", "autoclean"], check=False)
        subprocess.run(["sudo", "apt-get", "autoremove", "-y"], check=False)
    except Exception as e:
        print(f"{Colors.WARNING}[!] APT cleaning skipped or failed: {e}{Colors.ENDC}")

    print(f"{Colors.BLUE}[3/4]{Colors.ENDC} Flushing temporary directories (Tmp)...")
    try:
        subprocess.run("sudo find /tmp -mindepth 1 -delete", shell=True, check=False)
        subprocess.run("sudo find /var/tmp -mindepth 1 -delete", shell=True, check=False)
    except Exception as e:
        print(f"{Colors.WARNING}[!] Temp directories flushing failed: {e}{Colors.ENDC}")

    print(f"{Colors.BLUE}[4/4]{Colors.ENDC} Vacuuming old system journal logs...")
    try:
        subprocess.run(["sudo", "journalctl", "--vacuum-time=3d"], check=False)
    except Exception as e:
        print(f"{Colors.WARNING}[!] Journal logs vacuuming failed: {e}{Colors.ENDC}")

    print(f"\n\n{Colors.CYAN}{'=' * WIDTH}{Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}{' ' * 13}System cleaned and updated successfully! {Colors.ENDC}")
    print(f"{Colors.CYAN}{'=' * WIDTH}{Colors.ENDC}\n\n")
    
    input(f"{Colors.CYAN}Press Enter to return to menu...{Colors.ENDC}")


def main_menu():
    """
    Main execution loop and menu routing with spacious centered headers.
    """
    while True:
        clear_screen()
        print_banner("CYBERSECURITY MULTI-TOOL CLI", "Version 3.3", Colors.BLUE, "=")
        print(f"  {Colors.GREEN}[1]{Colors.ENDC} Password Strength Checker")
        print(f"  {Colors.GREEN}[2]{Colors.ENDC} Data & Number Converter")
        print(f"  {Colors.GREEN}[3]{Colors.ENDC} Local IP Address Generator")
        print(f"  {Colors.GREEN}[4]{Colors.ENDC} Encode and Decode text (CAESAR CIPHER)")
        print(f"  {Colors.GREEN}[5]{Colors.ENDC} System Cache & File Cleaner")
        print(f"  {Colors.FAIL}[0]{Colors.ENDC} Exit Program")
        print(f"\n{Colors.CYAN}{'=' * WIDTH}{Colors.ENDC}")

        user_choice = input(f"\n{Colors.BOLD}Select an option (0-5): {Colors.ENDC}").strip()
        
        if user_choice == "1":
            password_checker()
        elif user_choice == "2":
            data_converter()
        elif user_choice == "3":
            ip_generator()
        elif user_choice == "4":
            caesar_cipher_menu()
        elif user_choice == "5":
            system_cleaner()
        elif user_choice == "0":
            print(f"\n{Colors.GREEN}Exiting program. Stay secure! Goodbye! 👋{Colors.ENDC}\n")
            break
        else:
            print(f"\n{Colors.FAIL}[!] Invalid selection. Please enter a number from 0 to 5.{Colors.ENDC}")
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.ENDC}")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}[!] Program interrupted by user. Exiting safely...{Colors.ENDC}\n")
        sys.exit(0)
