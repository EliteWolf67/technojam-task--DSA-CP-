
n = int(input("Enter 'n': \n"))
k = int(input("Enter 'k': \n"))

for i in range(k):
    if(n%10 == 0):
        n = n/10
    else:
        n = n-1
        
print("'n':", n)
