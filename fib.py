a=int(input("enter the number to print the fib serise:-"))
b=0
c=1
print(b,end=" ")
print(c,end=" ")
while(a>0):
    s=b+c
    print(s,end=" ")
    b=c
    c=s
    a=a-1
print("all fib printed:-")
      