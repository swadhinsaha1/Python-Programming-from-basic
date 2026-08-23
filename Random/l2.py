# l1=[23,12, 41, 12, 56, 12, 78, 12, 72,56,16,98]

l=[]
n=int(input("Enter the length of the list= "))
for i in range(n):
    x=int(input("Enter the element="))
    l.append(x)

print(l)

m=[]

for i in l:
    temp=i
    rv=0
    while temp>0:
        r=temp%10
        rv=rv*10+r
        temp//=10
    m.append(rv)
print(m)