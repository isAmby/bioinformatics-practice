#open the file and read the lines
with open("Datasets/rosalind_ini5.txt", "r") as f:
    lines = f.readlines()

#write the odd-numbered lines to the output file
with open("Datasets/Outputs/output5.txt", "w") as output:
    result = lines[1::2]
    for line in result:
        print(line.strip(), file=output)