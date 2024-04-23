import random
import string

def generate_password(length):
    if length < 6:  # Minimum length check for security reasons
        print("Password length should be at least 6 characters.")
        return None

    # Characters to generate password from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generating a random password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():
    try:
        length = int(input("Enter the desired length of the password (min 6 characters): "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
