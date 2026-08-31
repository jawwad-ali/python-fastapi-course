## Control Flow


eligible_age_for_cnic = 18
current_age = 18.01
# current_age = 17.99
# current_age = 10

if current_age >= eligible_age_for_cnic:
    print("You are eligible for CNIC")
else:
    print("You are not eligible for CNIC")


### Grading system
grade = 80
if grade >= 90:
    print("A+")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Failed")


## Login System
email = "ali@gmail.com"
password = "123"

if email=="ali@gmail.com"  and password =="123":
    print("Login Successful")
else:
    print("Login Failed")