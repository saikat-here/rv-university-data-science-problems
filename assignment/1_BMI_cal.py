"""
Let’s put ourselves in the shoes of a childcare provider.
As childcare providers, we have an essential role in children’s lives by helping them learn and grow. You help children get the nourishment and energy they need to learn and grow by providing healthy meals. 


Also, keep in mind that preschoolers who eat a variety of healthy foods and play actively several times every day are less likely to be overweight or obese.

In this assignment, you will try to calculate a child's nutritions, using Python. This is a compulsory individual assignment wherein you will write Python code to take input from the user,  set various conditions, calculate BMI and calorie consumption, and submit the code.


Hints:
Create a child nutrition calculator based on the following tasks & conditions:
The calculator should be able to store the details of the child such as the name, age, gender, height and weight.
Calculate the BMI of the child using the standard BMI formula.
Display the minimum daily calorie requirement based on age. Use the below criteria to display the same:

 

Age b/w 0-2 years: 800 calories
Age b/w 2-4 years: 1400 calories
Age b/w 4-8 years: 1800 calories
Take as input what that child has eaten throughout the day and in what quantities.

 

Calculate the daily calorie consumption based on the following criteria:

Milk: 100 cal/ 100g
Egg: 155 cal/ 100g
Rice: 130 cal/ 100g
Lentils: 113 cal/ 100g
Vegetable: 85 cal/100g
Meat: 143 cal/ 100g
Next, compare the daily consumption with the recommended value and print if the child is undernourished or not.

 

Data for BMI Calculation:
                                                             BMI = weight/(height**2)*703

 

         Weight in pounds and height in inches 
"""
child_details = {}
child_calorie_details = {}

def take_input(msg, i_type):

    while True:
        user_i = input(msg)

        if i_type == "alpha":
            user_i_temp = user_i.replace(" ","")
            if user_i_temp.isalpha():
                return user_i
            print("Invalid input. Please try again")

        elif i_type == "number":
            if user_i.isnumeric():
                return int(user_i)
            print("Invalid input. Please try again")

        elif i_type == "gender":
            if user_i.lower() in ["male","female"]:
                return user_i
            print("Gender should be Male or Female")

def get_daily_calorie(age):

    if age > 0 and age <= 2:
        return 800
    elif age >2 and age <= 4:
        return 1400
    elif age > 4 and age <= 8:
        return 1800

def get_health_by_bmi(bmi):
    if bmi < 16 :
        return "Severely Underweight"
    elif bmi >= 16 and bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <25:
        return "Healthy"
    elif bmi >=25 and bmi <30:
        return "Overweight"
    elif bmi >= 30:
        return "Obese"

def calculate_cal():

    child_calorie_details["Milk"] = input("Please enter the milk consumption for the day (g): ") or "0"
    child_calorie_details["Egg"] = input("Please enter the Egg consumption for the day (g): ") or "0"
    child_calorie_details["Rice"] = input("Please enter the Rice consumption for the day (g): ") or "0"
    child_calorie_details["Lentils"] = input("Please enter the Lentils consumption for the day (g): ") or "0"
    child_calorie_details["Vegetable"] = input("Please enter the Vegetable consumption for the day (g): ") or "0"
    child_calorie_details["Meat"] = input("Please enter the Meat consumption for the day (g): ") or "0"

    cal =  (float(child_calorie_details["Milk"]) * 1) + (float(child_calorie_details["Egg"]) * 1.55) + (float(child_calorie_details["Rice"]) * 1.3)
    cal = cal + (float(child_calorie_details["Lentils"]) * 1.13) + (float(child_calorie_details["Vegetable"]) * 0.85) + (float(child_calorie_details["Meat"]) * 1.43)

    return cal

child_details["name"] =  take_input("Please enter the name of the child: ", "alpha")
child_details["name"] = child_details["name"][0].upper() + child_details["name"][1:]

while True:
    child_details["age"] = take_input("Please enter the age of the child: ", "number")
    if child_details["age"] < 0:
        print("Age can't be in negative. Please try again")
        continue
    elif child_details["age"] > 8:
        print("This program is designed for child upto 8 years. Please provide a correct age between 0 to 8 years")
        continue

    break

child_details["gender"] = take_input("Please enter the gender of the child: ", "gender")
child_details["height"] = take_input("Please enter the height of the child (inches): ", "number")
child_details["weight"] = take_input("Please enter the weight of the child (pounds ): ", "number")

child_details["BMI"] = (child_details["weight"]/(child_details["height"]**2))*703
#print(f"\nBMI of child is {child_details['BMI']}")
child_details["health"] = get_health_by_bmi(child_details["BMI"])

child_details["DailyCalReq"] = get_daily_calorie(child_details['age'])

#print(f"Minimum daily calorie requirement based on age is {child_details['DailyCalReq']}")


child_details["CalConsumption"] = calculate_cal()


print("********* Child Details ********* ")
print(f"Name: {child_details['name']}")
print(f"Age: {child_details['age']}")
print(f"Gender: {child_details['gender']}")
print(f"Height (inches): {child_details['height']}")
print(f"Weight (pounds): {child_details['weight']}")

print(f"\nChild BMI is {child_details['BMI']}")
print(f"Child is {child_details['health']}")
print(f"Daily require calorie is {child_details['DailyCalReq']}")
print(f"Today's consumed calorie is {child_details['CalConsumption']}")

if child_details['CalConsumption']  < child_details["DailyCalReq"]:
    print("\nChild is undernourished as calorie consumed is less than the recommendation")
else:
    print("Child is not undernourished")

