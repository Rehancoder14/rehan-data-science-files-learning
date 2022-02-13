#assignment 2 prob 1
def fahrenheigt(temp):
    cels = (temp * 9/5) + 32 
    return cels

boiling = 100
freezing = 0
print(f"The boiling point of water in fahrenheit is {fahrenheigt(boiling)} ")
print(f"The freezing point of water in fahrenheit is {fahrenheigt(freezing)}")



#assignment 2 prob 2
n = int(input("how many times would you like to run: "))
for i in range(n):
    print("Have a nice day.")






#assignment 3 prob 3

def calc_age(age,year):
    a = 100 - age
    b = year + a
    return b

name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter current year: "))
print(name, " Your age will turn into 100 in year ",calc_age(age,current_year))
