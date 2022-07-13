def is_twinprime(n):
    def is_prime(n):
        if abs(n) == 2: return False
        print(f'checking if {n} is prime')
        for i in range(2,abs(int(n/2))):
            print(f'checking divisibility of {i}')
            if n%i == 0:
                print(f'{n} is divisible by {i}, returning False')
                return False
            elif n%i != 0:
                continue
        print(f'{n} is prime, returning True')
        return True
    if is_prime(n) and is_prime(n-2):
        print(f'n is {n}')
        print(f'n-2 is {n-2}')
        return True
    elif is_prime(n) and is_prime(n+2):
        print(f'n is {n}')
        print(f'n+2 is {n+2}')
        return True
    else: return False

print(is_twinprime(0))