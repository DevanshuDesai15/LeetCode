class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0: # check if negative or not
            return False
        
        div = 1 # this could be 100 or 1000 or anything
        # how large it should be 
        while x>= 10* div: # if greater or equal to x
            div *= 10
            
        while x:
            right = x % 10 # to get right digit
            left = x // div # to get left digit
            
            if right != left: return False
            
            x = (x %div) // 10 # chop of the left and right digit
            div = div /100 # update div: when chop 2 digit so divide by 100
            
        return True