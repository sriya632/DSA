'''
Problem statement
Given an integer ‘n’, return first n Fibonacci numbers using a generator function.

Example:
Input: ‘n’ = 5

Output: 0 1 1 2 3

Explanation: First 5 Fibonacci numbers are: 0, 1, 1, 2, and 3.
Note:
You don't need to print anything. Just implement the given function.
'''
def generateFibonacciNumbers(n: int)->list[int]:
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

def main():
    n = int(input("Enter the number: "))
    result = generateFibonacciNumbers(n)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()