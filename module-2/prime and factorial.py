"""Check whether a user-provided integer is a prime number."""

def is_prime(number: int) -> bool:
    """Return True when number is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

def main() -> None:
    """Read an integer and display its prime-number status."""
    number = int(input("Enter an integer: "))

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()

