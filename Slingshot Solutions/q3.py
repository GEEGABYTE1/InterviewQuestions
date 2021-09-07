def fraction(string):
    string_split = string.split("+")
    denominators = []
    numerators = []

    for fraction in string_split:
        if fraction == '-':
            continue
        else:
            if fraction[0] == '-':
                numerator = int(fraction[1]) * -1
            else:
                numerator = int(fraction[0])
            denominator = int(fraction[-1])
          
            denominators.append(denominator)
            numerators.append(numerator)
    
    
    cm = 1
    for denominator in denominators:
        cm *= int(denominator)

    for denominator in range(len(denominators)):
        numerator = numerators[denominator]
        factor = cm // denominators[denominator]
        numerators[denominator] *= factor


    numerator_sum = 0
    for numerator in numerators:
        numerator_sum += numerator
    try:
        if cm % numerator_sum  == 0:
            denominator = cm // numerator_sum 
            numerator = numerator_sum // numerator_sum
    except ZeroDivisionError:
        denominator = 1
        numerator = 0

    return_string = '{}/{}'.format(numerator, denominator)
    return return_string


    



print(fraction('-1/2+1/2'))