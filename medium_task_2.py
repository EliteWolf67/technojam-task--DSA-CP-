
# Online IDE - Code Editor, Compiler, Interpreter

class Solution:
    def countPrimes(self, n: int) -> int:
        

        primes = [True for i in range(n)]
        i = 2
        while(i*i < n):
            if(primes[i] == True):
                for p in range(i*i, n, i):
                    primes[p] = False
            i += 1
        
        number_of_primes = 0
        for i in range(2, len(primes)):
            if primes[i]:
                number_of_primes += 1
        return number_of_primes
        
