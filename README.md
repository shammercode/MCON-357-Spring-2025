# MCON-357-Spring-2025
Exercises for the MCON-357 course for the Spring Semester  2025

# Git and GitHub Helpful tips
On MAC and Linux, you can use the following command to cache your GitHub credentials for a certain period of time. This way, you don't have to enter your username and password every time you push to GitHub.
- Install git credential manager:
```bash
brew tap microsoft/git
brew install --cask git-credential-manager-core
```
-verify installation
```bash
git-credential-manager-core --version

- configure git to use the credential manager
```bash
git config --global credential.helper manager
```
When you do push it will prompt for the token or asks to sign in via browser. This will save the token in the keychain



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
