import random 
import string

def create_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    # Initialize an empty string to hold the selected characters
    char_pool = ''
    
    # Add letters to the string
    if include_letters:
        char_pool += string.ascii_letters
    
    # Add digits to the string
    if include_numbers:
        char_pool += string.digits
    
    # Add punctuation to the string
    if include_symbols:
        char_pool += string.punctuation

    # Ensure at least one of above options is selected
    if not char_pool:
        raise ValueError("At least one character set must be selected")

    # Generate the password by randomly selecting characters from options
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Get user input for password length and character preferences
pwd_length = int(input("Enter the desired password length: "))
use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

# Generate the password based on user preferences
generated = create_password(pwd_length, use_letters, use_numbers, use_symbols)

# Display the generated password
print("Generated Password:", generated)
