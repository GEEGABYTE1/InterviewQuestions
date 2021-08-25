

def rainwater(heights):
    total_water = 0 
    for i in range(1, len(heights) - 1):
        left_bound = 0 
        right_boud = 0 

        for j in range(i + 1):
            left_bound = max(left_bound, heights[j])
        
        for j in range(i, len(heights)):
            right_bound = max(right_bound, heights[j])
        
        total_water += min(left_bound, right_bound) - heights[i]
    
    return total_water