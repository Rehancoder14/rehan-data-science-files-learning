def addnum(n):
    return n+n
print(addnum(5))

number = (1,3,4,5)
result =  map(addnum, number)
print(list(result))