# Knapsack Problem 👝

Problem: Imagine that you're a thief breaking into a house. There are so many valuables to steal - diamonds, gold, jelwelry, and more! But remember, you're just one person who can only carry so much. Each item has a weight and value, and your goal is to maximize the total value of items while remaining within the weight limit of your knapsack. This is called the knapsack problem. 

We will take into considertaion three paramters:
  - `weight_cap`: Totla amount of weight we can carry 
  - `weights`: Weights of all the items in an array
  - `values`: Values of all the items in an array

# Solutions ✅

  ## Recurision 🔄
  
  The brute force solution to this problem is to look at every subset of the items that has a total weight less than `weight_cap`. Then you simply take the maximum of those subsets, giving you the optimized subste with the highest value possible. We also take an additional parameter, `i`, that tells us where we are in the list of items. Additionally, we take into consideration three possibilities, 
  - 1) `weight_cap` or `i` are zero, meaning the knapsack can hold no weight, or there are no more items to look at. In either case, we return 0.
  - 2) The weight of the item we're looking at exceeds `weight_cap`, in which case we just move on, calling the function on the next item.
  - 3) If neither of the above are ture, that means we have to consider whether or not the item we are at (`i`) should be included in the optimal solution.

 ## Dynamic Programming Approach 🔮
 
 We can use memoization to store information instead of making duplicated calls. In this case, we will store our information in a 2D array that has a row for every item and `weight_cap + 1` number of columns where each element in the 2D array (*matrix*) represents a subproblem. The element at the bottom right will be the optimal solution. The rows represent the items we have seen and the columns represent how much weight the knapsack can hold.


# More Information 📕
Time Complexity of Recursion Solution: `O(2^n)`
Time Complexity of Dynamic Programming Approach: `O(n*weight_cap)` 

Made in Python 🐍
