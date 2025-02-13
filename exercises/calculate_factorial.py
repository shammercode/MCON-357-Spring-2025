# implement factorial_recursive method
def factorial_recursive(number):
    if number < 2:
        return 1
    return number*factorial_recursive(number-1)


def main():
    print("Factorial Computation Using Recursion")
    number = int(input("Enter a non-negative integer: "))
    while number < 0:
        number = int(input("Input was negative. Enter a non-negative integer: "))
    print(factorial_recursive(number))


if __name__ == "__main__":
    main()
