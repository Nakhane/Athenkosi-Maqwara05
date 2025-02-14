import secrets  # Importing the secrets module for generating secure random values
import string   # Importing the string module to access character sets

def generate_password(length=16):

    # Define the character set: letters (uppercase & lowercase), digits, and punctuation
    chars = (
        string.ascii_letters +  # Includes 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        string.digits +         # Includes '0123456789'
        string.punctuation      # Includes special characters like '!@#$%^&*()'
    )

    # Generate a random password by selecting 'length' characters from the character set
    return ''.join(secrets.choice(chars) for _ in range(length))

# Call the function to generate a password
password = generate_password()

# Print the generated password
print(f"Your new password is: {password}")