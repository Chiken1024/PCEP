def s(n: int) -> int:
  return n + s(n-1) if n > 0 else 0

print(s(10))