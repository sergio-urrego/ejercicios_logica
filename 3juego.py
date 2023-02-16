from os import system
pro=["yo","tu","el","nosotros","vosotros","ellos"]
ar=["o","as","a","amos","áis","an"]
er=["o","es","e","emos","éis","en"]
ir=["o","es","e","imos","ís","en"]

verbo=str(input("escriba el verbo a conjugar...\n"))
l=len(verbo)
t=verbo[-2:l]
b=verbo[:l-2]

if t=="ar":
    comb=ar
elif t=="er":
    comb=er
elif t=="ir":
    comb=ir

for i in range (len(pro)):
    print(pro[i],b+comb[i])
