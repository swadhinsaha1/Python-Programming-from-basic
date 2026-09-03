# Merging Two Dictionaries and Displaying Key-Value Pairs
d1={"name":"Swadhin","roll":23,"ph":987575343}
d2={"email":"abc@gmail.com","address":"Rampur","id":3425}
d3=d1|d2
for i in d3.keys():
    print(f"{i}:{d3[i]}")