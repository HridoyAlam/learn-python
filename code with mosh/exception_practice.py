try:
    age = int(input("Enter your age: "))
    income = 20000
    print(age)
    risk = income / age
    print(risk)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Something can't devided by zero")
