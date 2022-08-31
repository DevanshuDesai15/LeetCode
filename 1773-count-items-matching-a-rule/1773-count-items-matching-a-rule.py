class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d ={ 'type':0, 'color':1, 'name':2 }
        key = d[ruleKey]
        final=0
        
        for item in items:
            if item[key] == ruleValue:
                final +=1
        return final