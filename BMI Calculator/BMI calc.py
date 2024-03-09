"""
Create a command-line BMI calculator in Python. Prompt users for their weight (in kilograms) and height (in meters).
Calculate the BMI and classify it into categories (e.g., underweight, normal, overweight) based on predefined ranges. Display the BMI result and category to the user
"""

#BMI Caluculator
"""
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater
"""

weight = float(input("Enter your weight in kg :"))
height = float(input("Enter your height  in centimeteres :"))
height_in_meters = height / 100
BMI = weight / (height_in_meters**2)
print("BMI : {:0.2f}".format(BMI))

if(BMI < 18.5):
    print("You are severely underweight  " )
elif(BMI >= 18.5 and BMI    < 24.9):
    print("You are underweight " )
elif(BMI >= 24.9 and BMI < 30):
    print("You are overweight ")
else :
    print("You are Obese  " )
