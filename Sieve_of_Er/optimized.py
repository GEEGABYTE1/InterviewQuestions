import math
 
def sieve_of_eratosthenes (limit):
  
  if (limit <= 1):
    return []

  output = [True] * (limit+1)
 
  output[0] = False
  output[1] = False
 
  for i in range(2, math.floor(math.sqrt(limit))):
    if (output[i] == True):
      j = i ** 2   
 
      while j <= limit:
        output[j] = False
        j += i

  output_with_indices = list(enumerate(output))
  trues = [index for (index,value) in output_with_indices if value == True]
  return trues
 
primes = sieve_of_eratosthenes(20)
print(primes)