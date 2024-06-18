def is_prime(num):
    # If number is less than 2, it's not prime
    if num <= 1:
        return False
    
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# Example usage
number = 17
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
