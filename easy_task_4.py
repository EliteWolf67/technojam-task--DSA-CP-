
# Online IDE - Code Editor, Compiler, Interpreter


n = int(input("Enter 'n': \n"))
 
for i in range(n):
    entered_word = input()
    x = len(entered_word)
    if x <= 10:
        print(entered_word)
    else:
        print(entered_word[0] + str(x-2) + entered_word[-1])
