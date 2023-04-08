import random

name=input("Enter everybody's name separated by comma: ")
name_list=name.split(" ")
print(name_list)
random_choice=random.randint(0, len(name_list)-1)
print(f'{name_list[random_choice]} will pay the bill')