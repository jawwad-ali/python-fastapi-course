print(type(5))
print(type("Ali"))
print(type("5"))
print(type(True))
print(type("False"))

# 1. Comparison Operators
print(5 == 5)
print(4 == 5)

# Less than
print(4 < 5)

# Greater than
print(10 > 20)
print(18 >= 15)
print(22 >= 18)
print(12 >= 18)
print(18 >= 18)

## Logical Operator

### database value
email = "jamal@test.com"
password = "pak123"
age = 18

# AND operator (strict)
print(email == "jamal@test.com" and password == "pak123")
print(email == "Jamal@test.com" and password == "pak123" and age == 18)

# OR Operator
print(10 < 5 or 9 > 8 or 10 == 10 or 67 < 90)