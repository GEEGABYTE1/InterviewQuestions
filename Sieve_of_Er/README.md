# Sieve of Eratosthenes

Sieve of Eratosthenes is not really a problem, but it's an algorithm that is helpful to compute possible prime numbers giving a limit, `n`.

The algorithm was made or derived by Eratosthenes, a Greek mathematician born in the third century BCE.

# Algorithm Implementaion 👾
  
  ## Basic Implementation 
  
  The Algorithm works by first assuming that all numbers from `2` to `n` are not prime, and then succesfully makring them as *not* prime. Here are the steps of computing those prime numbers with our method: 
  - 1) Create a list of integers from `2` to `n`.
  - 2) Start with the smallest number in the list.
  - 3) Mark all the multiples of that number up to `n`
  - 4) Move to the next non-marked number and repeat this process until the entire list has been covered. 
  
  When the steps are complete, all the remaining non-marked numbers are prime. In our case, in Python, we have set a dictionary with the number as a key and their status (`True` or `False`). We set up two nested loops, the first one to iterate each element as the current smallest number, and the second one to iterate through the array again, but this time, to check if there are any multiples. If there are, then the algorithm will set the number as `False` and will continue traversing. This process goes on until the first loop has traversed the whole list. In other words, every multiple in the list of each number has been checked. At the end, we return the numbers that have their status as `True`, which means that there are prime since there were not multiple of any of the numbers to `n`. 
  
  For the edge cases, if the limit is `1` or `0`, the list will return an empty array.
 
 ## Optimizations 
 
  ### End Boundary Optimization
   In our basic implementation, the outer loop iterated from `2` to `n`. Thus, because the inner loop marks multiples of a base value, we only need to check individual numbers lower than the square root of `n`. 
   
 ### First Multiple
  In our basic implementation, the inner loop started checking multiples of 2 times the current number. However, we can skip a few checks starting the checks at `current^2`. 
 
 ### Pre-Marking all Even Numbers
  Since even numbers can never be prime as they can always be split by the number 2, there is no point of even adding even numbers to our base array. Hence, we must ignore those numbers and only compare odds as they have a higher chance of being prime. 
  
## Complexity 
  The Base Implementation Time Complexity: `O(n^2)`. However, with all the optimizations, the actual complexity of the algorithm is `O(n log (log n))`. This is because we need to take into consideration two operations: the creation of the array itself and incrementing along with the multiple marking loops. The creation of the array will take `O(n)` as we traverse through each number to `n`. The multiple marking happens in `O(n log (log n)) time`. The reasons for this, comes to down to some complex mathematics. 
  
  By definition, the number of times we mark a non-prime number is `n/2 + n/2 + ... + n/sqrt(n)`. It series begins with `n/2` because at the start, all the multiples of `2` are marked as non-prime (this will happen 50 times with a limit of 100, as each even number is marked). This process continues up until the squre root of `n`. At the end, through some mathematical proofs, the overall complexity gets generalized to `O(n log (log n ))` since this is larger than the `O(n)` array-creation time.
  

# More Information ✍🏻
 - `basic_implementation.py`: The basic implementation of the algorithm 
 - `optimized.py`: The optimized version of the algorithm 
 
 There is only one test case, but feel free to add more if needed.
 
 Made in Python 🐍


