# Here we are going to learn about conditional coding of if & else.....

isUserLoggedIn = True

if isUserLoggedIn:
    print("User is online.")     #Here this condition is true so "if" output will be printed.

else:
    print("User is offline.")

# Here we are checking if the user is online or not and on the basis of that we are printing different values.


userName = "Amrit"

if userName == "Raju":
    print("Amrit is online.")    #Here userName is not "Amrit" as we are checking for "Raju", so this condition will not be printed.
else:
    print("Wrong user.")         #Here we are checkin for Raju so this condition will be printed.