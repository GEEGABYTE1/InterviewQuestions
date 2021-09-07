
def miss_you(lst):
    sorted_lst = radix_sort(lst)
    max_val = sorted_lst[-1]
    if not 0 in lst:
        reference = list(range(1, max_val + 2))
    else:
        reference = list(range(max_val + 2))

    
    for val in range(len(reference)):
        try:
            if sorted_lst[val] == reference[val]:
                continue 
            else:
                return reference[val]
        except IndexError:
            return reference[val]







def radix_sort(lst):
    max_value = max(lst)
    max_exponent = len(str(max_value))
    being_sorted = lst[:]

    for exponent in range(max_exponent):
        position = exponent + 1 
        index = -position 
        digits = [[] for i in range(10)]

        for number in being_sorted:
            string_number = str(number)
            try:
                digit = string_number[index]
            except IndexError:
                digit = 0 
            
            digit = int(digit)
            digits[digit].append(number)
            being_sorted = []
            for numeral in digits:
                being_sorted.extend(numeral)
            
    return being_sorted


