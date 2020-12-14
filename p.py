i=int(input("enter number of terms"))
a = 0
b = 1     
count=0
if i<=0:
      print("not valid")
elif i==1:
    print(a)
else:
    print("The fibonacci series is:")
    while count<i:
        print(a)
        c = a + b
        a = b
        b = c
        count=count+1
    

