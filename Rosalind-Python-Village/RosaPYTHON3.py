# Practice with lists and strings
friends = ['aruzhan', 'batyrkhan', 'rauan', 'ilya']
friends[1] = 'alibek'
friends.append('Batyrkhan')
print(friends[1:3])

frststr = 'Money'
scndstr = 'population'
print(frststr[:4] + scndstr[4:])

#Problem solution
#Opening file and splitting the dataset into string and integers
with open("Datasets/rosalind_ini3(1).txt", "r") as f:
    dataset = f.read().strip()
    string, integers = dataset.splitlines()

a, b, c, d = map(int, integers.split())
with open("Datasets/Outputs/output3.txt", "w") as output:
    print(string[a:b + 1] + " " + string[c:d + 1], file=output)

