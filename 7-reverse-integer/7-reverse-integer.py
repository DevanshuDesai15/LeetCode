class Solution:
    def reverse(self, x: int) -> int:
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]  # Convert int -> Str
        else:
            strx = str(x)

        x = int(strx[::-1])  # Converting Str -> int
        
        return 0 if x > pow(2, 31) else x * negFlag # power range and else to print the output
    