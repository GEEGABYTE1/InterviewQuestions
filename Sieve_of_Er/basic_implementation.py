def sieve_of_eratosthenes(limit):
  true_indices = []
  array = [i for i in range(2, limit + 1)]
  dictionary = {}
  for number in array:
      dictionary[number] = True 
   
  for key, value in dictionary.items():
      if value == False:
          continue 
      else:
        for number in dictionary.keys():
            if number == key:
                continue
            elif number % key == 0:
                dictionary[number] = False 
            else:
                continue 
  for key, value in dictionary.items():
      if value == True:
          true_indices.append(key)

  return true_indices      






primes = sieve_of_eratosthenes(100000004)
print(primes) # should return [2, 3, 5, 7, 11, 13]