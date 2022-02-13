while True:
    num = input("Enter Your Name: ")
    if num.isalpha():
        print(num)
        break
    else:
        print("name cannot be integer")
        continue

a = 1
while a<6:
    print(a)
    a = a+1