# usually represent sequences
# the time complexity to delte the element at index i from an array of length n is O(n-i)
# key property of a list is that its dynamically resized, theres no bound as to how many values can be added to it. 

def even_odd(A):
  next_even, next_odd = 0, len(A) - 1
  while next_even < next_odd:
    if A[next_even] % 2 == 0:
      next_even += 1
    else:
      A[next_even], A[next_odd] = A[next_odd], A[next_even]
      next_odd -= 1
  print(A)

# even_odd([1,2,3,4])
# output: [4, 2, 3, 1] 

"""
- creating entries from the front is slow, try to append to the back
"""

def appending(Array, value):
  Array.append(value)
  print(Array)


# appending([1,2,3], 4)


# write a program that takes an array A and an index i into A, and rearranges the elements such that all elements less than A[i] appear first,
# followed by elements equal to the pivot, followed by elements greater than the pivot
RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
  pivot = A[pivot_index]
  # Keep the following invariants during partitioning:
  # bottom group: A[:smaller]
  # middle group: A[smaller:equal]
  # unclassified group: A[equal:larger]
  # top group: A[larger:]
  smaller, equal, larger = 0, 0, len(A)
  #keep iterating as long as there is an unclassified element
  while equal < larger:
    # A[equal] is the incoming unclassified element
    if A[equal] < pivot:
      A[smaller], A[equal] = A[equal], A[smaller]
      smaller, equal = smaller + 1, equal + 1
    elif A[equal] == pivot:
      equal += 1
    else: # A[equal] > pivot
      larger -= 1
      A[equal], A[larger] = A[larger], A[equal]
  print(A)

# dutch_flag_partition(3, [1,2,3,4,5,6,7])
# output : [1, 2, 3, 4, 6, 7, 5]

