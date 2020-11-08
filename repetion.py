a = list( input()) 
cou8nt = 0
max= 0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        cou8nt+=1
        if  max<=cou8nt:
            max=cou8nt
    elif a[i] !=a[i+1]:
        cou8nt=0

print(max+1)