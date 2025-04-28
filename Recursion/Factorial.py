# You are given an integer ’n’.

# Your task is to return a sorted array (in increasing order) containing all the factorial numbers which are less than or equal to ‘n’.

#  The factorial number is a factorial of a positive integer, like 24 is a factorial number, as it is a factorial of 4.

# Note:
# In the output, you will see the array returned by you.
# Example:
# Input: ‘n’ = 7

# Output: 1 2 6

from typing import * 
def factorialNnumbers(n: int) -> List[int]:
    i = 1
    fact =1 
    ans = []
    
    while fact <=n:
        ans.append(fact)
        i+=1
        fact*=i
    return ans

def main():
    n = int(input("Enter the number: "))
    result = factorialNnumbers(n)
    print(" ".join(map(str, result)))
    
if __name__ == "__main__":
    main()
    