# LeetCode
Solving leet-code problems everyday

### Problem number-9 
#### The Palindrom problem
Here I have solved this problem by converting the input into str as follows:


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]   // here first the string is reverse using reverse indexing 
        // so if normal str == reverse str then true
        
But it is mentioned that I don't have to convert it into string so i tried with:

## Solution2:

if x<0:
  return false

inputNum = x
newNum = 0
while x>0:
  newNum = newNum * 10 + x % 10
  x = x//10
return newNum == inputNum

## Solution3:

def isPalindrome(self, x: int) -> bool:
	if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
		return False
	
	result = 0
	while x > result:
		result = result * 10 + x % 10
		x = x // 10
		
	return True if (x == result or x == result // 10) else False
