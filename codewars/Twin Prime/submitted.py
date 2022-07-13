def is_twinprime(n):
    def is_prime(n):
        if abs(n) == 2: return False
        for i in range(2,abs(int(n/2))):
            if n%i == 0:
                return False
            elif n%i != 0:
                continue
        return True
    if is_prime(n) and is_prime(n-2):
        return True
    elif is_prime(n) and is_prime(n+2):
        return True
    else: return False