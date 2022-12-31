num = int(input("enter no."))
a = 0
for i in range (1,num):
    if num % i == 0:
        a = a+i
if a == num:
    print("yes, it's a perfect number")
else:
    print("No, it is not a perfect number")
