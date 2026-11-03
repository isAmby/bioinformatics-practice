with open('Datasets/rosalind_iprb.txt', 'r') as f:
    k, m, n = map(int, f.read().split())
    total = k + m + n
    pairs = total * (total - 1)
    rec_aa = n * (n - 1)
    Rec_Aa = ((m * n) + (n * m)) * 0.5
    AaAa = (m * (m - 1)) * 0.25
    recessive = rec_aa + Rec_Aa + AaAa
    prob = recessive / pairs
    Dominant = 1 - prob
with open('Datasets/Outputs/rosalind_iprb_output.txt', 'w') as out:
    print(Dominant, file=out)