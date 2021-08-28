
def dice_sum(aws):
    die_1 = [num for num in range(1, 7)]
    die_2 = range(1, 7)
    die_2_matrix_ref = [i for i in range(1, 7)]

    matrix = [[0 for i in range(1, 8)] for j in range(1, 8)]

    for lst_idx in range(len(matrix)):
        if lst_idx == 0:
            matrix[lst_idx] = [None] + [i for i in die_1] 
        else:
            matrix[lst_idx][0] = die_2_matrix_ref[0]
            die_2_matrix_ref.pop(0)
            counter = 1
            output1 = die_1[0]
            for output2 in die_2:
                possible_roll = (output1, output2)
                matrix[lst_idx][counter] = possible_roll
                counter += 1
            

            die_1.pop(0)
    
    nums = []
    comparision_row = 0
    row = 1
    column = 1
    while row != len(matrix[0]):
        if column == 7:                                         # Edge Cases 
            row += 1
            column = 1
        die_1_output = matrix[comparision_row][column]         # For Reference
        if die_1_output >= aws:
            break
        dies_output = matrix[row][column]
        dies_output_1 = dies_output[0]
        dies_output_2 = dies_output[1]
        
        ans = dies_output_1 + dies_output_2
        if ans == aws:
            nums.append(dies_output)
            row += 1
            column = 1
        else:
            column += 1
    
    print("Here are the possible permutations: {}".format(nums))
    base = 36 
    choices = len(nums)
    probability = (choices / base) * 100 
    print("The Probability of getting the sum {sum} is: {probability}%".format(sum=aws, probability=probability))

        

        


        
        




print(dice_sum(10))