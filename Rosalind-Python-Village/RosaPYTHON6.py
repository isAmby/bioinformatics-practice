#Practice Problem 6:

#create a dictionary 
gene_lengths = {
    "TP53": 19149,
    "BRCA1": 81189,
    "EGFR": 188307
}

# output the length of the BRCA1 gene
print(gene_lengths["BRCA1"])

#add new key-value and update the value of an existing key
gene_lengths['MYC'] = 43967
gene_lengths['TP53'] = 676767

#delete a key-value pair
del gene_lengths['EGFR']

#safe reading with "get" method
print(gene_lengths.get('INS', 0))
print(gene_lengths.get('TP53', 0))


#Solving problem 6

#create a dictionary, open the file and sort into the dictionary
dict = {}
with open("Datasets/rosalind_ini6.txt", "r") as f:
    words = list(f.read().split())
    for word in words:
        dict[word] = dict.get(word, 0) + 1

#write the dictionary to the output file in correct format for rosalind
with open("Datasets/Outputs/output6.txt", "w") as output:
    for key, value in dict.items():
        print(key + ' ' + str(value), file=output)
            