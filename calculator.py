num1=input("Enter your first number : ")
num2=input("Enter your second number : ")
op=input("Enter your choice Ex: +,-,/,*,**,//,% ")
if op=="+":
    print("Addition")
    add=float(num1)+float(num2)
    print("Your answer is : " +str(add))
elif op=="-":
    print("Substract")
    sub=float(num1)-float(num2)
    print("Your answer is : " +str(sub))
elif op=="*":
    print("Multiplication")
    mul=float(num1)*float(num2)
    print("Your answer is : " +str(mul))
elif op=="/":
    print("Divide")
    div=float(num1)/float(num2)
    print("Your anwer is : " +str(div))
elif op=="**":
    print("Power")
    power=float(num1)**float(num2)
    print("Your answer is : " +str(power))
elif op=="//":
    print("floor divison")
    floor=float(num1)//float(num2)
    print("Your answer is : " +str(floor))
elif op=="%":
    print("Modulus")
    modulus=float(num1)%float(num2)
    print("Your answer is : "+ str(modulus))
else:
     print("Invalid")
