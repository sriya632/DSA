'''
Problem statement
You are given two numbers ’x’(it’s a float), and ’n’(it’s a integer).

Your task is to calculate ‘x’ raised to power ‘n’, and return it.

The expected time complexity is ’O(logn)’, and the expected space complexity is ’O(1)’, where ‘n’ is the power to which the number should be raised.

Note:
In the output, you will see the number returned by you upto 6 decimal places.

Example:
Input: ‘x’ = 10, ‘n’ = 4

Output: 10000.000000

Explanation: On raising ‘x’ to the power of ‘n’, the result is 10000.
'''
def myPow(x: float, n: int) -> float:
    ''' We can use python built-in pow function, but we will implement our own version using recursion.'''
    if n == 0:
        return 1
    if x ==0:
        return 0
    if x ==1:
        return 1
    
    if n<0:
        return 1/myPow(x,-n)
    
    half = myPow(x, n//2)
    if n % 2 ==0:
        return half*half
    else: 
        return half*half*x
    
def main():
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))
    print(f"{myPow(x, n):.6f}")

if __name__ == "__main__":
    main()