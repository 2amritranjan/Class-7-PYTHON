# Here we are trying to make a fitness calculator using input function and variables with some use of if-else.

W = float(input("Enter your weight in kg:- "))
H = float(input("Enter your height in meters:- "))

BMI = W/(H**2)

if BMI >= 20 and BMI <= 25:
    print(f'Your BMI is {BMI} you are fit.')
else:
    print(f'Your BMI is {BMI} you are not fit.')
