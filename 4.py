weight=eval(input("please enter your weight by kg"))
height=eval(input("please enter your height by m")))
bmi=weight/height**2
print("your bmi is %.1f"%bmi)
if bmi<18.5:
    print("slim")
elif bmi>=24:
    print("overweight")
else:
    print("normal")
