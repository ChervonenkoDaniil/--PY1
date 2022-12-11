from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n=8) -> str:
    return ''.join(sample(list(ascii_uppercase) + list(ascii_lowercase) + list(digits), n))


print(get_random_password())
