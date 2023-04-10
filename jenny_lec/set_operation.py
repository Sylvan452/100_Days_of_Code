set1={'sylva','doris','abigail'}
set2={'tessy','beauty','iruo'}
set3=set1.union(set2)
print(set3)
set4=set2.union(set1)
print(set4)
set5=set1.intersection(set2)
print(set5)
print(set1.union(('othuke', 'frank')))
set1.update(set2)
print(set1)