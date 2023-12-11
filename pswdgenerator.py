import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please choose at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')
    print(f"Password saved to {filename}")

def main():
    print("Welcome to the Random Password Generator!")
    
    password_length = int(input("Enter the desired password length: "))
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_symbols)

    if generated_password:
        print("Generated Password:", generated_password)
        save_to_file = input("Do you want to save this password to a file? (y/n): ").lower()
        if save_to_file == 'y':
            save_password_to_file(generated_password)

if __name__ == "__main__":
    main()
