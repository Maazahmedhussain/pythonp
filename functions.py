# def greeting(x,y=11):
#     for i in range(1,y,1):
#         print("hi",x)
# greeting("maaz",10)


def greeting(x,y):
    return x*y
a=greeting(5,5)
print(a)
if a>10:
    print("hello")
else:
    print("bye")