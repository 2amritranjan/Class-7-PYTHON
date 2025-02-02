# Here we are creating SI Calculator using input function and variable.

p = int(input("Enter your principle amount:- "))
r = int(input("Enter your rate of interest:- "))
t = int(input("Enter your time duration:- "))

si = (p*r*t)/100

print(f'Your total interest is Rs. {si}')