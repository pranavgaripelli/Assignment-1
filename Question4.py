it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies1=("Infosys","TCS")

it_companies.update(it_companies1)
print(it_companies)

it_companies.remove("IBM")
print(it_companies)

"""If there is no item to remove the remove() method raise error simultaniously, 
If there is no item to remove then discard() method will not rise error """

C=A.union(B)
print(C)

X=A.intersection(B)
print(X)

Z=A.issubset(B)
print(Z)

Y=A.isdisjoint(B)
print(Y)

AB=A.union(B)
print(AB)
BA=B.union(A)
print(BA)

D=A.symmetric_difference(B)
print(D)

Q=A.clear()
W=B.clear()
print(Q,W)


ages=[19,22,19,24,20,25,26,24,25,24]
S=set(ages)
print(S)
print(len(ages),len(S))