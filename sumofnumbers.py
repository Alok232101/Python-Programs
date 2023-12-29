s,e=input("Enter starting and ending number sepearted by comma : ").split(",")
s=int(s)
e=int(e)
S=0
while s<=e:
    S=S+s
    s=s+1

print(S)