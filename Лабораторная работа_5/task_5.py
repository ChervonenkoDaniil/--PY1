from random import choice
import string


def get_random_password(n=8) -> str:
    return ''.join([choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(0, n+1)])


print(get_random_password())
