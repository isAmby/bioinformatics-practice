# Practice with lists and strings
friends = ['aruzhan', 'batyrkhan', 'rauan', 'ilya']
friends[1] = 'alibek'
friends.append('Batyrkhan')
print(friends[1:3])

frststr = 'Money'
scndstr = 'population'
print(frststr[:4] + scndstr[4:])

#Problem solution
probstr = str(input('Enter a string: '))
a, b, c, d = map(int, input('Enter an integers: ').split())
print(probstr[a:b+1], probstr[c:d+1])