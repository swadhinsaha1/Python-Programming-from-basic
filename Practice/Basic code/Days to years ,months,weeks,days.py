x=int(input("Enter the numbers of days="))
years=x//365
temp1=x%365
month=temp1//30
temp2=temp1%30
weeks=temp2//7
r_days=temp2%7
print(x,"days has",years,"years",month,"months",weeks,"weeks and",r_days,"days")