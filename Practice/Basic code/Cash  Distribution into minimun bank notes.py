x=int(input("Enter the cash amount="))
n500=x//500
temp1=x%500
n200=temp1//200
temp2=temp1%200
n100=temp2//100
temp3=temp2%100
n50=temp3//50
temp4=temp3%50
n20=temp4//20
temp5=temp4%20
n10=temp5//10
temp6=temp5%10
n5=temp6//5
temp7=temp6%5
n2=temp7//2
temp8=temp7%2
print("500 motes=",n500)
print("200 motes=",n200)
print("100 motes=",n100)
print("50 motes=",n50)
print("20 motes=",n20)
print("10 motes=",n10)
print("5 coins=",n5)
print("2 coins=",n2)
print("1 coins=",temp8)

