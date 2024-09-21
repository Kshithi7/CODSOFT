import random # to randonly select the letters/characters
import string # to call predefined set of characters

#defining the main function of the code
def create_password(length, letters=True, numbers=True, symbols=True):
    #Declare a empty string to hold the selected characters
    char_pool = ''
    
    # Add letters to the string
    if letters:
        char_pool += string.ascii_letters # ascii leters are predefined in the module
    
    # Add digits to the string
    if numbers:
        char_pool += string.digits # predefined set of character in the string module
    
    # Add punctuation to the string
    if symbols:
        char_pool += string.punctuation #call the predefined function from string module

    # Ensure at least one of above options is selected
    if not char_pool:
        raise ValueError("At least one character set must be selected")

    # Generate the password by randomly selecting characters from options
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Get user input for password length and character preferences
length = int(input("How long should be your paasword ?: "))
letters = input("Include letters? (yes/no): ").lower() == 'yes'
numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

# Generate the password based on user preferences
generated = create_password(length, letters, numbers, symbols)

# Display the generated password
print("Generated Password:", generated)
