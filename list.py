# li=[1,2,3,4,5,True,'fsa']
# print(li[1:4])
# print()
# li.insert(4,100)
# li.pop(3)
# li.remove("fsa")
# li.clear()
# del(li)

# print(li.append('hi'))
# for i in li:
#     print(li)
    
    
li=[10,20,5,8.0,80,30]
ages=[]
for i in li:
    if i>=18:
        ages.append(i)
        print("you are elgible to vote",i)
    else:
        print("not elogible",i)
    print(ages)
    