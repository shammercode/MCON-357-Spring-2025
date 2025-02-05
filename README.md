# MCON-357-Spring-2025
Exercises for the MCON-357 course for the Spring Semester  2025

## Exercise for Module2 - Introduction to Python

### Recursive Factorial Calculation**

#### **Objective:**
Write a Python program that computes the factorial of a given non-negative integer using recursion.

#### **Instructions:**
1. Define a function called `factorial_recursive(n)` that:
    - Takes a non-negative integer `n` as input.
    - Returns `1` if `n` is `0` or `1` (base case).
    - Otherwise, recursively calls itself to compute `n * factorial_recursive(n - 1)`.

2. Implement a `main()` function that:
    - Prompts the user to enter a non-negative integer.
    - Ensures the input is valid (i.e., non-negative).
    - Calls the recursive function to compute the factorial and prints the result.

#### **Example Output:**
```
Factorial Computation Using Recursion
Enter a non-negative integer: 5
The factorial of 5 is: 120
```

#### **Bonus Question:**
Modify the program to handle non-integer inputs gracefully by displaying an error message.
