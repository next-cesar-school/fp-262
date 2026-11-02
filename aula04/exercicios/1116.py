# -*- coding: utf-8 -*-

i = int(input())

for _ in range(i):
  a, b = input().split()
  a, b = int(a), int(b)

  if b == 0:
    print('divisao impossivel')
  else:
    print(f'{a / b:.1f}')
