import random

firstname = ['mark', 'matt', 'john', 'chris', 'tom', 'phil', 'todd', 'bill', 'robert', 'steve']
lastname = ['baker', 'clayton', 'kudell', 'smith', 'foo', 'usher', 'demarco', 'fender']

name = firstname[random.randint(0,len(firstname)-1)] + ' ' + lastname[random.randint(0,len(lastname)-1)]
print(name)