with open('Datasets/rosalind_ini4(1).txt', 'r') as f:
    a, b = map(int, f.read().split())
odd_sum = []
for i in range(a, b + 1):
    if i % 2 != 0:
        odd_sum.append(i)
result = sum(odd_sum)

with open('Datasets/Outputs/output4.txt', 'w') as output:
    print('Sum of odd integers:', result, file=output)