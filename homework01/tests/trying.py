def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    i = 2
    if n == 2:
        return True
    else:
        while n % i != 0 and i <= n:
            i += 1
            return True
            break
        else:
            return False
print(is_prime(319))