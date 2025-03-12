#create a variable called Weight to store the value of a person’s weight (in kg).
Weight = float(input("please enter your weight in kg"))
#create a variable called Height to store the value of height (in m).
Height = float(input("please enter your height in m"))
#caculate BMI
BMI=Weight/Height**2
print(f"Your BMI is {BMI}")
if BMI >30:
    print("You are obese.")
elif BMI <18.5:
    print("You are underweight.")
else:
    print("You are normal weight.")