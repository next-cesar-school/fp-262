# -*- coding: utf-8 -*-

nums = []

for _ in range(10):
  n = int(input())

  if n <= 0:
    nums.append(1)
  else:
    nums.append(n)

i = 0
for n in nums:
  print(f'X[{i}] = {n}')
  i = i + 1
