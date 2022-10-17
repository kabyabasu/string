print("enter your string 1")
s1 = input()
print("enter your string 2")
s2 = input()
def checkRot(s1,s2):
    
    for i in range(len(s1)-1):
        s3 = s1[i+1:]+s1[:i+1]
        if s3 == s2:
            print(f"{s1} is a iso form of {s2}")
            break

        
    else:
        print(f"{s1} is not a isoform of {s2}")
    


checkRot(s1,s2)
