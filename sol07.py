# s=input("enter a sen: ")
# u=l=int()
# u=l=0
#
# for x in s:
#     if x.isupper():
#         u=u+1
#     else:
#         l=l+1
#     print("upper", u )
#     print("lower",l)

# s=input("enter a sen: ")

def upper_lower(s):
     u=l=0

     for x in s:
        if x.isupper():
         u=u+1
        elif x.islower():
         l=l+1

     return " upper " + str(u) + " lower " + str(l)
print(upper_lower("I love you"))