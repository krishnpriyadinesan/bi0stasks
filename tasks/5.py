string=input()
s=sorted(string)
even=[]
odd=[]
upper=[]
lower=[]

for i in s:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append()
    elif(int(i)%2==0):
        even.append()
    else:
        odd.append()
s=lower.join(s)
s=upper.join(s)
s=odd.join(s)
s=even.join(s)
             
