# secrets_module have funcions to returns random values
# the secrets module is different from the random module, as
# the values returned by secrets are more secure

from secrets import SystemRandom
import secrets
import string

# get all character in the keyboard
all_characters = ''.join(
    [string.ascii_letters, string.digits, string.punctuation])

# print(all_characters)

# Transfer the random number generation system of secrest module
# to "random"
random = secrets.SystemRandom()

random_password = random.choices(all_characters, k=14)
print(''.join(random_password))

# Or:

print(''.join(SystemRandom().choices(all_characters, k=12)))
