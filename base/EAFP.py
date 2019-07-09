class tester():
    pass

tester = tester()
d = {}    
words = ['a','d','a','c','b','z','d',tester]

for w in words:    
    try:
        d[w] += 1    
    except KeyError:    
        d[w] = 1
print(d)