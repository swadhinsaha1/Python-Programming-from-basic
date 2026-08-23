l=[2,35, 44,54,35,76,45,86,35,56]

# m=[23,34.6,"Swadhin",True]
# print(m)
##--a list can contain anything in it(integer,float,string,boolean etc...)

# print(l)
# #--to print the list

# l.append(8)
# print(l)
# #--to add some thing in the end of the list

# l.reverse()
# print(l)
# #--used to reverse the list

# l.sort()
# print(l)
# #--to sort the list in assending order(by default)

# l.sort(reverse=True)
# print(l)
# #--to sort the list in desending order

# print(l.index(54))
# #--used to know the index of the specific number
# #--here I want to know the index of 54

# print(l.count(35))
# # #--used to know the specific number is available for how many times
# # #--here I want to know that 35 is present for the how many times

# g=l.copy()
# print(g)
# #--there is a "g" another blank list and all the elements of the list "l" is copyed in it 

# g=[]
# g=l.copy()
# print(g)
# #--same thing but for the better explanation

# l.insert(2,5754)
# print(l)
# #--here,I want to put 5754 in index 2

# k=[345,6543,7678,5654]
# v=l+k
# print(v)
# #--a type of merging two or more than two lists

# k=[345,6543,7678,5654]
# l.extend(k)
# print(l)
# #--it looks like append but it has some differences which will discuss below----

# #The difference between append and extend---->
# l = [1, 2, 3]
# l.append([4, 5])
# print(l)

# l = [1, 2, 3]
# l.extend([4, 5])
# print(l)

# # append() → adds ONE item
# # extend() → adds MULTIPLE items from another iterable


# l=[23,34,23,432,345,654,324,32]
# print(l)
# l.pop()#wiothout any inofrmation deleted from the back of the list 
# print(l)    
# m=[23,34,23,432,345,654,324,32]
# m.pop(2)
# #with index deleted from the list 
# print(m) 
# n=[23,34,23,432,345,654,324,32]
# n.remove(432)
# #with element deleted fromthe list 
# print(n)   
