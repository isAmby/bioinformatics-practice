with open('Datasets/rosalind_fib.txt', 'r') as f:
    n, k = map(int, f.read().split())
    rabbits = [0] * (n + 1)
    rabbits[1] = 1
    rabbits[2] = 1
    for i in range(3, n + 1):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]
with open('Datasets/Outputs/rosalind_fib_output.txt', 'w') as out:
    print(rabbits[n], file=out)