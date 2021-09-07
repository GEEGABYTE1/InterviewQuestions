
def int_target(lst, target):
    counter = 0 
    summation = 0 
    counter_forwards = 1
    answer = False
 



    for i in range(len(lst)):
        tracker = 0
        if i == 0:
            if lst[i] == target:
                counter += 1
                break 
            else:
                continue 
        else:
            while tracker != len(lst):
                element = lst[i:counter_forwards]
                for num in element:
                    summation += num 
                if summation == target:
                    counter = len(element)
                    return counter 
                else:
                    counter_forwards += 1
                
                tracker += 1
                summation = 0
            
           
    return counter



print(int_target([1, 4, 4], 1))
    

