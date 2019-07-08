
# prob:09

# def s_two_number(a,b):
#     c=a+b
#     return c
# print(s_two_number(2,3))


#  prob:10
# def ing_to_st(a):
#    # a=int()
#    c=str(a)
#    return c
# print(ing_to_st(10))

# prob:11
#
# def s_str(a,b):
#     # c=int(a)+int(b)
#     c = a+b
#     return c
# print(s_str("2","5"))

# prob:12
# def even_no(lst):
#     # lst=[]
#     x=0
#     for x in lst:
#         if x%2==0:
#             x=x+1
#     # return x.append('.')
#     return x
# # print(even_no'("[10,11,12]")'
# # print(even_no(10))

# def even_no(*x):
#     lst=[]
#     count=0
#     for i in x:
#         if i%2==0:
#             count= count+1
#     # return x.append('.')
#     return count
# # print(even_no('10','20','31'))
# print(even_no(10,20,31))

def even_no(*x):
    lst=[]
    # count=0
    for i in x:
        if i%2==0:
            # continue
            pass
            # count= count+1
    # return x.append('.')
    return i
print(even_no(10,20,39))