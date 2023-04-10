tuple1=(12,5,6,8,'sylva',True) #immutable
print(tuple1[1])
print(type(tuple1))
print(tuple1[-1])
tuple2=(5,2,5)
print(type(tuple2))
print(tuple1[1:4])
print(len(tuple1))
tuple3=(tuple1,tuple2) #nested turple
print(tuple3)
print(tuple3[0])
print(len(tuple3))
tuple4=tuple1 + tuple2
print(tuple4)
print(max(tuple2))