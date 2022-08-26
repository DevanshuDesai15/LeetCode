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


if x<0:
  return false

inputNum = x
newNum = 0
while x>0:
  newNum = newNum * 10 + x % 10
  x = x//10
return newNum == inputNum
