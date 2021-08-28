# Dice Permutations

Problem: Given two dice, and a specific sum, finding the possible outcomes from rolling two die that sum to the specific number. Also find the probability of those results occuring. 

# Solution 
For my solution, I looked more towards the dynamic programming approach. Instead of nesting two for loops and compare each number side by side, I used a matrix for reference. The comparisions work the same as a typical nested loop, however, it allowed for some several optimizations.
  
  ## Optimizations 
  
  ### Optimization 1 - Sum Greater than 12
  The first optimization is to see if the sum is within the domain of the max sum made by the two dice. Since the max sum of the two dice can only be twelve (6 on one die and 6 on another), anything bigger would not be possible as there aren't any other numbers bigger than 6. Therefore, we can create an edge case that would ignore any input that is bigger than 12. This reduces the number of iterations to check. 
  
  ### Optimization 2 - If we have already found the two numbers 
  On both dices, there is only one number from each die that can be added to match the desired number. After we have found those two numbers, traversing the matrix would not be necessary, at least for that one side of the die. Hence, instead of just traversing the same side of the die until we have seen ever face, we will traversing that die, when we have found our desired number. This approximately reduces the number iterations by a factor of 2 on average. 
  
The Time Complexity for constructing the Matrix: `O(n * f)`. Where `n` represents each side of die 2 and `f` represents each side of die 1 for each complete traversal of die 2.
The Time Complexity for traversing and searching: `O(n (desired_sum / 6)`. Where `n` represents the other 6 faces of the die, and the quotient represents average number of searches.

# More Information 
There are many ways to implement this algorithm or to code a solution. However, this solution was mainly created due for its purpose of dynamic programming practice. 

Made in Python
