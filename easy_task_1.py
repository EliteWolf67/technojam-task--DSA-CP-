
# Online IDE - Code Editor, Compiler, Interpreter

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        arr = []
        arr.append(first)
        
        i=0
        for x in encoded:
            arr.append(arr[i] ^ x)
            i=i+1    
        return arr
        
