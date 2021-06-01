import os


# Factorial
def factorial(x):
    if x == 1:
        return 1
    return factorial(x - 1) * x


# Fibonacci
def fibonacci(n):  # not suitable for working with Fibonacci numbers
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Palindrome
def isPalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])


# Recursive folder traversal
path = 'task_0/folderRecursive'


def folderTraversal(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('We go down', path + '\\' + i)
            folderTraversal(path + '\\' + i, level + 1)
            print('We come back', path)


folderTraversal(path)
