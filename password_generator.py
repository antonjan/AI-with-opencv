
import secrets
import string

pw_length=8
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars
pwd = ''
pw_strong = False

while not pw_strong:
    pwd = ''
    for i in range(pw_length):
    pwd += ''.join(secrets.choice(alphabet))
    if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2):
       pw_strong = True

print('password = ', pwd)
