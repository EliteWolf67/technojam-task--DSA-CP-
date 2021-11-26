
# Online IDE - Code Editor, Compiler, Interpreter

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        students.sort()
        seats.sort()
        x = len(seats)
        
        total = 0
        # use 'abs' function for finding 'absolute' difference to avoid negative values in answer
        
        for i in range(x):
            total = total + abs(seats[i]-students[i])
        
        return total
