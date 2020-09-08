a=int(input("Type your frist numb ---> "))
b=int(input("Type your second numb ---> "))
if(a!=2):
    print("*"+"*"*(a-2)+"*")
    for i in range (b-2):
       print("*" + " " * (a - 2) + "*")
    print("*"+"*"*(a-2)+"*")
elif (a!=1):
   print("*" + " " * (a - 2) + "*")


else:
    print("*")

