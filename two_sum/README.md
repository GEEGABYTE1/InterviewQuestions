# Two Sum 

Problem: Given an array, return an array or tuple of two numbers that equal to a given value. 

# Solution 

With the two pointer method, we traverse the list both ways simulatenously, hence, creating linear time. We have two cases to progress throughout the solution, 
    - 1) If the summation of the left element and the right element are smaller than or equal to the target, than we add the two numbers to the returned lst if the summation is equal to the target, otherwise, we add 1 to the left_pointer to progress the list.
    - 2) If the summation is bigger than the target, we subtract one from the pointer to continue traversing the right side. 

*Note*: The left pointer starts at 0 and the right pointer starts at -1. Notice how we start at both ends of the list and progress our way towards opposite ends.


# More Information

Time Complexity: `O(n)`

Made in Python 🐍