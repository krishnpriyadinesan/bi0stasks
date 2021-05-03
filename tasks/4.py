list=[]
seclownames=[]
scores=set()

for _ in range(int(input())):
    name=input()
    score=float(input())
    list.append([name, score])
    scores.add(score)
        
seclowscores=sorted(scores)[1]

for name,score in list:
    if (score==seclowscores):
        seclownames.append(name)

for name in sorted(seclownames):
    print(name, end='\n')
