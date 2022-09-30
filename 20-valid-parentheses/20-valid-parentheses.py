class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closeToOpen = { ")" : "(", "]" : '[', "}" : "{" }
        
        for c in s:
            if c in closeToOpen: # if is a closing parantheses
                if stack and stack[-1] == closeToOpen[c]: # stack is not empty
                    # stack[-1] is last value added in stack
                    stack.pop() 
                else:
                    return False
            else: # if we not get closing parantheses
                stack.append(c)
        # after going throight every value stack can only return true if stack is empty
        return True if not stack else False