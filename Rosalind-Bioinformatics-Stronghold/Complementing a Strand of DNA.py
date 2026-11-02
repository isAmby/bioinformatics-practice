with open("Datasets/rosalind_revc.txt", "r") as f:
    dna = f.read().strip()
    revc = dna[::-1].translate(str.maketrans("ATCG", "TAGC"))
with open("Datasets/Outputs/rosalind_revc_output.txt", "w") as out:
    print(revc, file=out)