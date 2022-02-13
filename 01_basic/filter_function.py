def start_with_A(s):
    return s[0] == "A"
fruit = ["Apple","orange","Asparagus","banana"]
l1 = list(filter(start_with_A, fruit))
print(l1)


age = (12,45,14,15,54)
def age_count(x):
    if x>18:
        return True
    else: 
        return False