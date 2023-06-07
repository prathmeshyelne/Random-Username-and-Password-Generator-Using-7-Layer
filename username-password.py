import random
import string
import hashlib

# Layer 1 - Random Name
def generate_random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Layer 2 - Unique Identifier
def generate_unique_identifier(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Layer 3 - Leet Speak Conversion
def convert_to_leet_speak(username):
    leet_conversion = {'e': '3', 'o': '0', 's': '5', 'a': '4', 'i': '1'}
    return ''.join(leet_conversion.get(char, char) for char in username)

# Layer 4 - Special Characters
def add_special_characters(username):
    special_characters = string.punctuation
    return username + random.choice(special_characters)

# Layer 5 - Random Word
def generate_random_word():
    dictionary = ['apple', 'banana', 'carrot', 'dragon', 'elephant', 'friday', 'guitar', 'hockey', 'island']
    return random.choice(dictionary)

# Layer 6 - Case Variation
def vary_case(password):
    return ''.join(random.choice((str.upper, str.lower))(char) for char in password)

# Layer 7 - Salted Hashing
def generate_salted_hash(username, password):
    salted_string = username + password + 'salty_salt'
    return hashlib.sha256(salted_string.encode()).hexdigest()

# Generate random username and password
random_name = generate_random_name(6)
unique_identifier = generate_unique_identifier(4)
username = random_name + unique_identifier

leet_username = convert_to_leet_speak(username)
username_with_special_chars = add_special_characters(leet_username)

random_word = generate_random_word()
password = random_word + unique_identifier

password_with_varying_case = vary_case(password)
hashed_password = generate_salted_hash(username, password_with_varying_case)

print("Username:", username_with_special_chars)
print("Password:", password_with_varying_case)
print("Hashed Password:", hashed_password)
