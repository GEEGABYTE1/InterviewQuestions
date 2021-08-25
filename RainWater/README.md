# Capturing Rainwater


Problem: Imagine a very heavy rainstorm over a highway that has many potholes and cracks. The rainwater will collect in the empty spaces in the road, creating puddles. Each puddle can only be as high as the road around it, as any excess water will just flow away. Calculate how much rainwater would be trapped in the empty spaces. 

# Solutions

To get the amount of rainwater for each hole, we will find the different between the lower of the highest bars to its left and right, and the height of the index itself, assuming that our input is an array (which it is).

 - `water_at_index = min(highest_left_bound, highest_right_bound) - height_of_index`

## Naive Solution 
For the naive solution, we loop through all the elements and create two nested loops to iterature the left side and the right side. After collecting the *bounds* of each side, we move on to finding the difference with the expression above.

 - Time Complexity: `O(n^2)`

## Optimized Solution 

The optimized solution uses the two pointer approach. The pointers will start at each end of the array and move in towards each other. We have two cases to progress in the list:
 - 1) If the left pointer height is smaller or equal to the right pointer height, then we increase then we set the left bound to the max between the left bound and the height at left pointer. We also add the difference between the updated left bound and the height at left pointer to the rainwater total. Last but not least, we add one to the right left pointer to progress the traversal of the left side.
 - 2) If the left pointer height is not smaller or equal to the right pointer, then we do same things as the first case, but with the right bound and height. However, instead of adding one to the right pointer at the end, we will subtract one in order to bring the index closer into the middle to progress the traversal. 
  
 - Time Complexity: `O(n)`

# More Information 

- Both solutions have a space complexity of `O(1)` 
- `optimal.py` is the optimized solution
- `rainwater.py` is the naive solution 

Made in Python 🐍
