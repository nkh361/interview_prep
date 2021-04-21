def parity(x):
  result = 0
  while x:
    result ^= x & 1
    x >>= 1
  return result # The time complexity is O(n) where n is the word size

def parity(x):
  result = 0
  while x:
    result ^= 1
    x &= x - 1 # drops lowest set bit of x
  return result
