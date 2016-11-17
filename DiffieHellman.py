# /usr/bin/python
import math

"""
Prompt user for a Prime Number and store the input in p.
Prompt user for a primitive root of p and store the input in r.
Prompt user for Alice’s private key and store the input in a.
Prompt user for Bob’s private key and store in b.
Calculate Alice’s public key (x = ra mod p), Calculate Bob’s public key (y = rb mod p).
Assume public values x and y are exchanged.
Calculate Alice’s shared private key ( ka = ya mod p). Calculate Bob’s shared key (kb = xb mod p). Is ka = kb?
"""


def is_prime(num):
    """
    Checks to see if the number entered is prime
    Check to see if remainder is zero
    from 1 and sqrt(2)

    :return: boolean : if prime number or not
    """
    if num == 0 or num == 1:
        return False

    value = abs(int(num))

    # print(math.sqrt(value))
    root = math.ceil(math.sqrt(value))
    # print(root)

    # we already know number
    for i in range(2, root + 1):
        # check and see if there is a remainder
        # print(i, ",", value, ":", value % i)
        if value % i == 0:
            # if it divides with no remainder
            # its not a prime number
            return False

    return True


def prompt_prime():
    """
    Prompts user for prime number

    :return: prime number
    """
    user_input = 0

    while not is_prime(user_input):
        user_input = int(input("Please Enter Prime Number >>>  "))

    return user_input


def gcd(a, b):
    """
    Find greatest common denominator

    :return:
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def prompt_primitive(factor1):
    """
    Prompt user for a primitive root of p and store the input in r.

    :return:
    """
    user_input = 0

    while gcd(factor1, user_input) != 1:
        user_input = int(input("Please enter a primitive root of {} >>>   ".format(factor1)))

    return user_input


def prompt_private_key():
    """
    Prompt person for key
    :return: int : private key
    """
    return abs(int(input("Please Enter Private Key >>>   ")))


def calculate_key(key, p, r):
    """
    Calculate public key

    y = r*private_key % p

    :param key:
    :param p: prime number
    :param r: ordered factor of prime number
    :return: int : public key
    """
    return (r**key) % p


def run():
    """
    Main function for this script
    :return:
    """
    # Prompt user for a Prime Number and store the input in p.
    p = prompt_prime()

    # Prompt user for a primitive root of p and store the input in r.
    r = prompt_primitive(factor1=p)

    # Prompt user for Alice’s private key and store the input in a.
    alice_private_key = prompt_private_key()

    # Prompt user for Bob’s private key and store in b.
    bob_private_key = prompt_private_key()

    # Calculate Alice’s public key (x = ra mod p),
    alice_public_key = calculate_key(alice_private_key, p, r)

    # Calculate Bob’s public key (y = rb mod p).
    bob_public_key = calculate_key(bob_private_key, p, r)

    # Assume public values x and y are exchanged.

    # Calculate Alice’s shared private key ( ka = ya mod p).
    alice_shared_private_key = calculate_key(alice_private_key, p, bob_public_key)

    # Calculate Bob’s shared key (kb = xb mod p). Is ka = kb?
    bob_shared_private_key = calculate_key(bob_private_key, p, alice_public_key)

    print("Alice's Shared Private Key: {}".format(alice_shared_private_key))
    print("Bob's Shared Private Key: {}".format(bob_shared_private_key))
    print("Are the keys equal? {}".format(bob_shared_private_key == alice_shared_private_key))

    if bob_shared_private_key == alice_shared_private_key:
        print("{} is their shared secret".format(alice_shared_private_key))
    else:
        print("Alice slaps Bob for not getting the right key")


if __name__ == '__main__':
    run()
