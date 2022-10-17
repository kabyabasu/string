print("enter your string 1")
s1 = input()
print("enter your string 2")
s2 = input()
def checkRot(s1,s2):
    

s3 = s1+s1

if s3.find(s2) == True:
    print(f"{s1} is a isoform of {s2}")


else:
    print(f"{s1} is not a isoform of {s2}")
    


checkRot(s1,s2)
