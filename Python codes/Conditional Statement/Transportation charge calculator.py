# ~Up to 10 kg → ₹20 per kg
# ~Next 20 kg (11–30 kg) → ₹10 per kg
# ~Next 20 kg (31–50 kg) → ₹8 per kg
# ~More than 50 kg → ₹5 per kg
weight=int(input("Enter the weight of the parcel="))
if weight<=10:
    charge=weight*20
elif weight<=30:
    charge=(10*20)+(weight-10)*10
elif weight<=50:
    charge=(10*20)+(20*10)+(weight-30)*8
else:
   charge=(10*20)+(20*10)+(20*8)+(weight-50)*5
print("The final price for shipping=",charge)   