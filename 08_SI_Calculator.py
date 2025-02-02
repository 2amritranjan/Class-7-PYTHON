# Here we are creating SI Calculator using input function and variable.

p = float(input("Enter your principle amount:- "))
r = float(input("Enter your rate of interest:- "))
t = float(input("Enter your time duration:- "))

si = (p*r*t)/100

print(f'Your total interest is Rs. {si}')