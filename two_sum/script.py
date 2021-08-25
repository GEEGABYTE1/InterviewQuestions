
def two_sum(lst, target):
    sorted_lst = sorted(lst)
    left_pointer = 0
    right_pointer = -1
    returns_lst = []

    while left_pointer != len(lst) and right_pointer != len(lst) * -1:
        left_elm = sorted_lst[left_pointer]
        right_elm = sorted_lst[right_pointer]
        summation = left_elm + right_elm 

        if summation <= target:
            if summation == target:
                returns_lst.append((left_elm, right_elm))
            left_pointer += 1
        else:
            right_pointer -= 1
    
    return returns_lst
    


lst = [6, 3, 2, 5, 4, 1, 7]

print(two_sum(lst, 11))
        