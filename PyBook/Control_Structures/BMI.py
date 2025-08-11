'''Program to evaluate BMI and determine weight status'''
height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)  # Calculate BMI
if bmi < 18.5:
    print("Your BMI {} indicates you are underweight.".format(bmi))
if bmi>=18.5 and bmi<25:
    print("Your BMI {} indicates you are normal weight.".format(bmi))
if bmi>=25 and bmi<30:
    print("Your BMI {} indicates you are overweight.".format(bmi))
if bmi >= 30:
    print("Your BMI {} indicates you are obese.".format(bmi))