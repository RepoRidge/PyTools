import string
import random
import pyperclip

# Codici di escape ANSI per il colore del testo
GREEN = '\033[92m'
RESET = '\033[0m'

def generate_password(length=8, use_special_chars=True, use_uppercase=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    characters_pool = lowercase_letters
    if use_uppercase:
        characters_pool += uppercase_letters
    if use_special_chars:
        characters_pool += special_chars

    password = ''.join(random.choice(characters_pool) for _ in range(length))

    while not (any(char in lowercase_letters for char in password) and
               any(char in uppercase_letters for char in password) and
               any(char in digits for char in password) and
               any(char in special_chars for char in password)):

        password = list(password)
        if not any(char in lowercase_letters for char in password):
            password[random.randint(0, length - 1)] = random.choice(lowercase_letters)
        if use_uppercase and not any(char in uppercase_letters for char in password):
            password[random.randint(0, length - 1)] = random.choice(uppercase_letters)
        if not any(char in digits for char in password):
            password[random.randint(0, length - 1)] = random.choice(digits)
        if use_special_chars and not any(char in special_chars for char in password):
            password[random.randint(0, length - 1)] = random.choice(special_chars)
        
        password = ''.join(password)

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_special_chars, use_uppercase)
    print("Your generated password is:", GREEN + password + RESET)  # Stampa la password in verde

    copy_to_clipboard = input("Do you want to copy the password to clipboard? (yes/no): ").lower() == 'yes'
    if copy_to_clipboard:
        pyperclip.copy(password)
        print("Password copied to clipboard!")

    create_file = input("Do you want to create a file with the password? (yes/no): ").lower() == 'yes'
    if create_file:
        with open("password.txt", "w") as file:
            file.write(password)
        print("Password saved to password.txt file!")

if __name__ == "__main__":
    main()
