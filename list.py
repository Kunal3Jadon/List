#1..WAP to print sum of negative elements of list
l=list(eval(input()))
s=0
for i in l:
    if i<0:
        s+=i
print(s)
#2..WAP to print sum of even and odd index elements of list
l=list(eval(input()))
s=0
s1=0
for i in range(len(l)):
    if i%2==0:
        s+=l[i]
    else:
        s1+=l[i]
print("sum of odd index elements",s)
print("sum of even index elements",s1)

#3..WAP to swap first elements of two lists
l1=list(eval(input()))
l2=list(eval(input()))
temp=l1[0]
l1[0]=l2[0]
l2[0]=temp
print(l1)
print(l2)
#4..WAP to swap first element of first list with last element of second list and vice versa
l1=list(eval(input()))
l2=list(eval(input()))
l1[0],l2[-1]=l2[-1],l1[0]
l2[0],l1[-1]=l1[-1],l2[0]
print(l1)
print(l2)
#5..WAP to print border elements of a matrix
l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        n=int(input())
        l1.append(n)
    l.append(l1)
for i in range(3):
    for j in range(3):
        if i==0 or i==2 or j==0 or j==2:
            print(l[i][j])
        else:
            print(" ")

#6..WAP to print diagonal elemens of matrix
l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        n=int(input())
        l1.append(n)
    l.append(l1)
for i in range(3):
    for j in range(3):
        if i==j:
            print(l[i][j])
#7..WAP to print anti diagonal element of matrix
l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        n=int(input())
        l1.append(n)
    l.append(l1)
for i in range(3):
    for j in range(3):
        if j==(2-i):
            print(l[i][j])
#8..WAP to print upper half of matrix
l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        n=int(input())
        l1.append(n)
    l.append(l1)
for i in range(3):
    for j in range(3):
        if i<=j:
            print(l[i][j])
#9..WAP to print lower half of matrix
l=[]
for i in range(3):
    l1=[]
    for j in range(3):
        n=int(input())
        l1.append(n)
    l.append(l1)
for i in range(3):
    for j in range(3):
        if i>=j:
            print(l[i][j])
#10..WAP to create a new list with elements greater than 18 from existing list
l=list(eval(input()))
l1=[]
for i in l:
    if i>18:
        l1.append(i)
print(l1)
