import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
  letters = string.ascii_letters
  nbs = string.digits
  special = string.punctuation

  pass_chars = letters
  if numbers:
    pass_chars += nbs

  if special_characters:
    pass_chars += special

  password = ""
  meets_criteria = False
  has_number = False
  has_special = False

  while not meets_criteria or len(password) < min_length:
    pwd_char = random.choice(pass_chars)
    password += pwd_char

    if pwd_char in nbs:
      has_number = True
    elif pwd_char in special:
      has_special = True

    meets_criteria = True
    if numbers:
      meets_criteria = has_number

    if special_characters:
      meets_criteria = meets_criteria and has_special
  return password

def main():
  length = int(input("Enter the length of the password: "))
  has_number = input("Do you want numbers in the password? (y/n): ").lower() == "y"
  has_special = input("Do you want special characters in the password? (y/n): ").lower() == "y"
  password = generate_password(length, has_number, has_special)
  print(f"The generated password is : {password}")

main()
