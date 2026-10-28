nums = [1, 2, 3, 4, 5, 6, 50]

quantidade = len(nums)
removido = nums.pop()
maiusculo = 'exemplo'.upper()

print(maiusculo)

if quantidade > 4:
    print('Esta lista tem 4 ou mais elementos')
else:
    print('Esta lista tem menos de 4 elementos')

print(f'Item removido: {removido}')