a, b = map(int, input('Enter two integers: ').split())
odd_sum = []
for i in range(a, b + 1):
    if i % 2 != 0:
        odd_sum.append(i)
print('Sum of odd integers:', sum(odd_sum))