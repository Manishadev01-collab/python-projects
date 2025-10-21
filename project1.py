# // Random password generator

# collect user preferences 
# -length
# -should contain uppercase
# -should contain special 
# -should contain digit

# get all available characters 
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid 










import random 
import string

def generate_password():
    # 1. Get and validate the desired length
    while True:
        try:
            length_input = input("Enter the desired password length (minimum 4): ").strip()
            length = int(length_input) 
            if length >= 4:
                break
            else:
                print("Password length must be at least 4 characters. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number for the length.")
    
    # 2. Get character set preferences
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    include_digits = input("Include digits (0-9)? (yes/no): ").strip().lower() == "yes"

    # 3. Define the character sets and ensure at least one set is chosen
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    special = string.punctuation if include_special else ""
    digits = string.digits if include_digits else ""
    
    # Start with mandatory lowercase characters (good practice for complexity)
    all_characters = lower + uppercase + special + digits
    
    if not all_characters:
        # Fallback if the user says 'no' to all, which shouldn't happen 
        # since 'lower' is always included, but a safety check.
        print("Error: No character types selected. Cannot generate password.")
        return
        
    # 4. Enforce inclusion of selected types and build the password
    password = []
    required_chars = [] # To ensure at least one of each selected type is present

    # Add at least one character of each selected type
    if include_uppercase:
        required_chars.append(random.choice(string.ascii_uppercase))
    if include_special:
        required_chars.append(random.choice(string.punctuation))
    if include_digits:
        required_chars.append(random.choice(string.digits))
        
    # Always ensure a lowercase character is included
    required_chars.append(random.choice(string.ascii_lowercase))

    # Fill the rest of the password length
    remaining_length = length - len(required_chars)
    if remaining_length < 0:
        # This can happen if the required length is too small relative to the number of types selected.
        # Since we enforce min length of 4 and have at most 4 required_chars, this shouldn't trigger
        # but it's a safety net.
        remaining_length = 0

    # Add the rest of the characters randomly from all selected sets
    password.extend(required_chars)
    password.extend(random.choices(all_characters, k=remaining_length))

    # 5. Shuffle the list to ensure randomness and convert to a final string
    random.shuffle(password)
    final_password = "".join(password)
    
    # 6. Output the final password
    print("\nGenerated Password: ✨ **" + final_password + "**")

# Start the function execution
generate_password()


