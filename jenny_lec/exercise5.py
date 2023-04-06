age = int(input('What is your age? '))
years_left= 90-age
days_left= years_left * 265
month_left= years_left * 12
weeks_left= years_left *52

print(f"You have {days_left} days, {weeks_left} weeks and {month_left} months left.")