f=open('3.txt','r')
l=f.readlines()
print(l)
a='012'
p=0
b=0
for i in l:
    for m in i:
        if m in a:
            print(l[l.index(i)-1])
        if m.isdigit():
            b=b+1
            m=int(m)
            p=p+m
print(p/b)





































# a=list()
# for i in l:
#     if i!=i[-1]:
#         i=i[:-1]
#         a.append(i)
# print(a)
# n=list()
# p=list()   #цифры
# for m in a:
#     if m.isdigit():
#         p.append(m)
#     else:
#         n.append(m)
# print(p)
# print(n)
# c=dict(zip(n,p))
# print(c)
# for i in c:
#     if int(c.get(i))<3:
#         print(i)
# d=0
# for i in c.values():
#     i=int(i)
#     d=d+i
# print(f'средний балл в классе {d/3}')
# f.close()







