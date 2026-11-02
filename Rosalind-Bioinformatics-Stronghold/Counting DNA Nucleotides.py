with open("Rosalind-Bioinformatics-Stronghold/Datasets/rosalind_dna.txt", "r") as f:
    dna = f.read().strip()
    
with open("Rosalind-Bioinformatics-Stronghold/Datasets/Outputs/rosalind_dna_output.txt", "w") as out:
    print(dna.count("A"), dna.count("C"), dna.count("G"), dna.count("T"), file=out)
