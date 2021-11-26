# technojam-task--DSA-CP-

A bit about myself:-

Hi! My name is Talal Zaffar and I'm a first year student in GU.
I am passionate about tech and I love to code. The reason of why I wanna join TechnoJam is I'm looking for like minded people with whom I can, just, talk to I guess. 
Don't know if it's just my bad luck, but I haven't been able to find anyone who shares my interests in my class since joining. Kinda ironic considering we're doing a CS course, but that's another story in itself. There's still a lot I need to learn and a lot I want to learn. And I'm sure being a part of TechnoJam will give me the chance to learn a lot from the members. 

Below is my attempt to write about my approach and algorithms of the programs. To be honest, I did have to look up stuff online as I was finding it pretty challenging to do these on my own. Being a first year student, who's barely come to grips with the languages, these questions were honestly not very easy IMO. 
I've tried my level best to do them all by myself, but I'd be lying if I said I did.


************************-----------**************************------------***************************


Approach and Algorithms of the problems:-

#easy_task_1 

The logic I used here was to use the xor operator on the first element of the array with the elements in the encoded array, to get the original array back. 
Had to look up how exactly the XOR operator is used before arriving at the solution.

#easy_task_2

The logic I used here was to first sort the elements in both the lists. Then I initialized a for loop to find the absolute difference of the elements in both the lists, and sum that to the total required at the end. Made a mistake initially by not sorting the elements in the list, which obviously didn't give the required output at the start. 


#easy_task_3

Not too sure what to write here, I initialized a for loop for the values in 'k' and used an if-else block according to what was asked in the question, i guess.

#easy_task_4

Again, initialized a for loop for the elements of the entered word and used an if-else block. Based on the conditions specified in the question, concatenated the first and last letter of the word with the length of entered word - 2. 
Had to look up how to accesss the last element of the list, which can be done by using the [-1] function.

#easy_task_5

#medium_task_1

Initialized the width of the container as 'l' and 'r' between the index of the two lines to begin with. The area of the required container would be in the form of a rectangle, so to find it, initialized a while loop with the condition that the height of the figure should be the minimum of the two lines from either end. 
To find the max area, initialized an if-else block and set the condition that the 'pointer' from either end would come 'inside' after every calculation. In the end, displayed the max area using the max function in the result.
Found this a bit tricky, and had to look it up to make sure I was understanding the question correctly. 

#medium_task_2

Again, had to look up the "sieve of eratosthenes" to get linear time complexity as leetcode wasn't accepting my previous solution, which had a time complexity of n^2, if I'm not wrong.

The entire code is based on that principle, which states that the multiples of prime numbers are constants. So initialized a for loop, after setting a boolean condition in which all the numbers were first marked as primes. This then marked off the multiples of prime numbers in the given range as composites. The ones which weren't marked, were the required prime numbers, which were then sumed up to get the required result. 

#medium_task_3

Honestly, found this way out off my league at the moment. 
I might revisit it once someone explains it to me!












