set1={'sylva','doris','abigail'}
set2={'tessy','beauty','iruo'}
set3={'oke','blessing'}
print(set1.difference(set2))
print(set1 ^ set2)
set2.symmetric_difference_update(set1)
print(set2)
