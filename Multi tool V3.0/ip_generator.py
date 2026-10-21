"""
Generates a list of target IP addresses for a given subnet range.
"""

def x():
    print("\n\n" + "-" * 46 + "\n\n")
    print("        [3] LOCAL IP ADDRESS GENERATOR")
    print("\n\n" + "-" * 46 + "\n\n")

    subnet = input("\n\nEnter network prefix (Example: 192.168.1): ").strip()

    try:
        print("\n\n")
        start_host = int(input("Enter start host (Example: 1): "))
        print("\n\n")
        end_host = int(input("Enter end host (Example: 10): "))

        # التحقق من أن النطاق منطقي
        if start_host > end_host:
            print("\n\n[!] Start host cannot be greater than end host.\n\n")
            return
        
        # التحقق من أن القيم ضمن نطاق IPv4 الصحيح (0 إلى 255)
        if not (0 <= start_host <= 255 and 0 <= end_host <= 255):
            print("\n\n[!] Host values must be between 0 and 255.\n\n")
            return
        
        print("\n\n\n--- Generated Target IP Addresses ---\n\n")
        ip_list = []
        
        for host in range(start_host, end_host + 1):
            ip = f"{subnet}.{host}"
            ip_list.append(ip)
            print(f"  • {ip}")
        
        print(f"\n\nSuccessfully generated {len(ip_list)} IP addresses.\n\n")
        
    except ValueError:
        print("\n\n[!] Host boundaries must be valid integers.\n\n")

if __name__ == "__main__":
    x()
