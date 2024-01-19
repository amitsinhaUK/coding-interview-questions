#
# Interview question: Code the fibonacci sequence using recursion and using an iterative method
# Solution Type: Initial solution, Time O(n), Space O(n)
# Code Author: Amit Sinha
#


def iterative_fib(n):
    # Create starting value of 1, 1 in-case of iteration
    fib_list = [1, 1]
    
    if n < 2:
        return n
    
    # We start at 2 because we already have the first 2 values of the list (1 and 1)
    for i in range (3, n+1):
        fib_list.append(fib_list[i-2] + fib_list[i-3])

    return fib_list[n-1]


def recursive_fib(n):
    if n < 2:
        return n
    else:
        value = recursive_fib(n-1) + recursive_fib(n-2)
        return value

print(f"Recursive result: {recursive_fib(3)}")
print(f"Iterative result: {iterative_fib(3)}")

