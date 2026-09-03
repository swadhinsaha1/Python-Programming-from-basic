#Eligibility criteria--------
# Maths marks ≥ 65
# Physics marks ≥ 55
# Chemistry marks ≥ 50
# If the above are true, then either:
# Total of all three subjects ≥ 190 OR
# Total of Maths + Physics ≥ 140

math=int(input("Marks of maths="))
physics=int(input("Marks of physics="))
chemistry=int(input("Marks of chemistry="))
if (math>=65 and physics>=55 and chemistry>=50):

    if ((math+physics+chemistry)>=190) or ((math+physics)>=140):
        print("You are eligible")
    else:
        print("you are not eligible")    

else:
    print("you are not eligible")    