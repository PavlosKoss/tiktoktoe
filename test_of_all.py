a = [1,3,4,1]
b = [1,2,3,4,5,6,7,8,9,0]
# true αν όλα τα στοιχεία του a υπάρχουν στο b
c = all(j in b for j in a)
print(c)


def a_fuction():
    return "something"

print(eval("a_fuction()"))


