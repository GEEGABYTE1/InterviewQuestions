def efficient_solution(heights):
  total_water = 0
  left_pointer = 0
  right_pointer = len(heights) - 1
  left_bound = 0
  right_bound = 0

  # Write your code here
  while left_pointer < right_pointer:
    left_height = heights[left_pointer]
    right_height = heights[right_pointer]

    if left_height <= right_height:
        left_bound = max(left_bound, left_height)
        total_water += abs(left_bound - left_height)
        left_pointer += 1
    else:
        right_bound = max(right_bound, right_height)
        total_water += abs(right_bound - right_height)
        right_pointer -= 1
    
  return total_water
  




test_array = [4, 2, 1, 3, 0, 1, 2]
print(efficient_solution(test_array))
# Print 6