height=input('Enter all height separated by a space: ')

height_list=height.split()
count=0
for i in height_list:
    count=count+1
for i in range(0,count):
    height_list[i]=int(height_list[i])
total=0
for i in height_list:
    total+=i
avg=total/count
print(round(avg))
