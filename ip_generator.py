import random
import ipaddress
from colorama import Fore, Style

# Function to generate a single random IP
def generate_random_ip():
    """
    Generates a random IP in string format.
    """
    ip_segments = []
    for _ in range(4):
        ip_segments.append(str(random.randint(0, 255)))
    return ".".join(ip_segments)

# Function to determine whether an IP address is private or public
def determine_ip_type(ip):
    """
    Determines whether the specified IP is private or public.
    """
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            return f"{Fore.RED}Private (IPv4){Style.RESET_ALL}"
        else:
            return f"{Fore.GREEN}Public{Style.RESET_ALL}"
    except ValueError:
        return "Invalid IP Address"

# Prompting the user for the number of IPs to generate
while True:
    try:
        num_ips = int(input("How many random IPs do you want to generate? "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Generating and printing the IPs
ip_list = []
for _ in range(num_ips):
    random_ip = generate_random_ip()
    ip_type = determine_ip_type(random_ip)
    ip_list.append(random_ip)
    print(f"IP: {random_ip} - Type: {ip_type}")

# Ask the user if they want to save the IPs to a text file
choice = input("Do you want to save the IPs to a text file (ip.txt)? (y/n): ").strip().lower()

if choice == 'y':
    try:
        with open('ip.txt', 'w') as file:
            for ip in ip_list:
                file.write(ip + '\n')
        print("IPs have been successfully saved to ip.txt")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Pause to view the generated IPs
input("Press ENTER to exit...")
