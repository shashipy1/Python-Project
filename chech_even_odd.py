num = int(input("Enter the number:"))
if (num % 2) == 0:
    print("Even")
else:
    print("Odd")


yr = int(input("Enter the number:\n\t"))
if (yr % 4) == 0:
    print("leap year")
else:
    print("Not leap year")


# Fine largest number
n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))
n3 = int(input("Enter the number:"))
if (n1 >= n2) and (n1 >= n3):
    print("n1 is large number")
elif(n2 >= n1) and (n2 >= n3):
    print("n2 is large")
else:
    print("n3 is large")

num = int(input("Enter the number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            num=True
            break
if num:
    print("NUMBER IS NOT PRINE")
else:
    print("NUMBER IS PRINE")

# primr number
lower = 200
upper = 500

print("Prime numbers between", lower, "and", upper, "are:")
if num>1:
    for i in range(lower,upper+1):
        if n>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
                else:
                  print(num)
                
   