class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        firstCell = int(s[1])
        secondCell = int(s[4])+1
        l=[]
        
        for ch in range(ord(s[0]), ord(s[3])+1):
            for i in range(firstCell, secondCell):
                l.append(chr(ch)+str(i))
        return l