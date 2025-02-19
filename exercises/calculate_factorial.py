import sys


def factorial_recursive(number: int) -> int:
    """
    This method finds the factorial of a non-negative integer input.
    It does so by calling itself recursively, returning the product
    of the passed argument and the factorial of the integer below it.
    Parameters:
        number: int
            int to calculate its factorial
   Returns:
        int
            factorial of number
    """
    if number < 2:
        return 1
    return number*factorial_recursive(number-1)


def factorial(number: int) -> int:
    """
  This method finds the factorial of a non-negative integer input
  passed as an argument and then returns the solution.
  Parameters:
      number: int
          int to calculate its factorial
 Returns:
      int
          factorial of number
  """
    sum = 1
    while number >= 2:
        sum *= number
        number -= 1
    return sum


def main():
    print("Factorial Computation Using Recursion")
    input_str = input("Enter a non-negative integer: ")
    value, error_message = process_input(input_str)
    while value is None:
        input_string = input(error_message + " Enter a non-negative integer: ")
        value, error_message = process_input(input_string)
    print("Factorial of " + str(value) + " found with recursion: " + str(factorial_recursive(value)))
    print("Factorial of " + str(value) + " found iteratively: " + str(factorial(value)))


def process_input(input_str: str) -> (int, str):
    """
    This method takes a string as a parameter and returns it as an int if the
    string holds a non-negative integer below the recursion limit, with an empty string
    in a tuple. Otherwise, it returns none with the error message.
    Parameters:
        input_str: str
            string to check
    Returns:
        (int, str)
            int if valid message with empty string or none and error message
    """
    error_message = ''
    value = None
    try:
        value = int(input_str)
        if value < 0:
            return None, "Number cannot be negative."
        if value >= sys.getrecursionlimit()-1:
            return None, "Number must be lower than" + str(sys.getrecursionlimit()-1) + " for our calculation."
    except ValueError:
        error_message = "Number must be an integer."
        return value, error_message
    return value, error_message


if __name__ == "__main__":
    main()
