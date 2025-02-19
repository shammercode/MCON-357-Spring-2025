# implement factorial_recursive method
def factorial_recursive(number):
    if number < 2:
        return 1
    return number*factorial_recursive(number-1)


def main():
    print("Factorial Computation Using Recursion")
    number= -1;
    while number < 0:
        try:
            number = int(input("Enter a non-negative integer: "))
        except ValueError:
            print("Number is not an integer.")

    print(factorial_recursive(number))


if __name__ == "__main__":
    main()
