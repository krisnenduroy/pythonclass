# i=int()
# list=[]
# x= input("enter a value"  ).split(',')
# for i in x:
#     if(int(i)%2!=0):
#         i=i**i
#     # else:
#     #     pass
# print(",".join(str(i)))

# val=input().split(",")
# s_num=( x*x for x in val if int(x)%2!=0)
# # print(",".join(str(s_num)))
# print(s_num)

# val=input().split(",")
# s_num=( x for x in val if int(x)%2!=0)
# # print(",".join(str(s_num)))
# print(s_num)

# x=int()
# val=int(input(x))
# s_num=[ x**x for x in val.split(",") if (int(x)%2!=0)]
# print(",".join(s_num))
# print(s_num)
# x=int()
# val=int(input())
# val=input()
# s_num=[ x for x in val.split(",") if (int(x)%2!=0)]
# print(",".join(s_num))

def square():
   val=input()
   s_num=[ x for x in val.split(",") if (int(x)%2!=0)]
     # return (s_num ,s_num**2)
   return s_num
#     print(",".join(s_num))
square(11)