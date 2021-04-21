# a palindromic string is one which reads the same when it is reversed

def is_palindromic(s):
  # note that s[~i] for i in [0, len(s) - 1] is s[-(i+1)]
  return all(s[i] == s[~i] for i in range(len(s) // 2)

print(is_palindromic("cat"))
