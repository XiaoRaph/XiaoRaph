def factorial(n):
  """Calculates the factorial of a non-negative integer."""
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def is_palindrome(s):
  """Checks if a string is a palindrome."""
  s = s.lower().replace(" ", "")
  return s == s[::-1]

def fibonacci_sequence(n):
  """Generates the Fibonacci sequence up to n terms."""
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    sequence = [0, 1]
    while len(sequence) < n:
      next_term = sequence[-1] + sequence[-2]
      sequence.append(next_term)
    return sequence
