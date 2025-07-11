#1
import datetime
x = datetime.datetime.now()
name = ("what's your name:")
age = int(input("which year you were born:"))
age2 = x.year - age
print(age2)
#2
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])
#3
txt = 'MsaatmiazD'
print(txt[-1::-2])
print(txt[::2])
#4
txt = "I'am John. I am from London"
print(txt[txt.index('London'):])
#5
name = input("Write your word:")
print(name[::-1])
#6
vowels = ['a', 'e', 'o', 'u', 'i']
text = input("Enter smth:")
count = sum(text.lower().count(vowel) for vowel in vowels)
print(count)
#7
values = list(map(int, input('Enter your numbers: ').split()))
max_value = max(values)
print(max_value)
#8
word = input('Enter you word:')
if word == word[::-1]:
    print("It is palidrome")
else:
    print("It is not palindrome")
#9
email = input("enter you email:")
print('Your domain is', email[email.index('@'):])
#10
import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Character sets
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # Special characters

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_chars = letters + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
password = generate_password(12)
print("Generated password:", password)


