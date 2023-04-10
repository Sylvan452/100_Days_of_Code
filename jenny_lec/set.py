set1={3,6,9,43,'sylva',True,12.4}
print(set1)
#set are immutable
#set are not acess via index
#duplicate are not allowed
#slicinh not allowed
set2={} #dictionart
print(type(set1))
print(type(set2))
set3=set() #empty set
set1.add(99)
print(set1)
set1.remove(99)
print(set1)
set1.union(set1,set2)
print(set1)