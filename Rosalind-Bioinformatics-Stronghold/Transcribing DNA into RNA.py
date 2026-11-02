with open("Rosalind-Bioinformatics-Stronghold/Datasets/rosalind_rna.txt", "r") as f:
    dna = f.read().strip()
    rna = dna.replace("T", "U")
with open("Rosalind-Bioinformatics-Stronghold/Datasets/Outputs/rosalind_rna_output.txt", "w") as out:
    print(rna, file=out)