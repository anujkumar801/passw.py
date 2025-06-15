import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return ""

    # All possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function
def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)

        if password:
            print("\n Your generated password is:\n" + password)

    except ValueError:
        print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
