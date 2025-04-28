''' 
Problem statement
Determine if a given string ‘S’ is a palindrome using recursion. Return a Boolean value of true if it is a palindrome and false if it is not.
Note: You are not required to print anything, just implement the function. Example:
Input: s = "racecar"
Output: true
Explanation: "racecar" is a palindrome.
'''
def isPalindrome(s: str) -> bool:
   
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
   
    return isPalindrome(s[1:-1])

def main():
    s = input("Enter the string: ")
    result = isPalindrome(s)
    print(result)

if __name__ == "__main__":
    main()