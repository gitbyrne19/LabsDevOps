import datetime


print("Hello git!")
print("Hello world")
print("Learning about git diff. ")
print(f"Today is {datetime.date.today()}")


def greet(name):
    return f"Hello, {name}! Welcome to Git and Github."

print(greet("Luke"))

print("This line was added directly on GitHub.")

<<<<<<< HEAD
print("This line was added locally.")
=======

print("Another line added on GitHub.")
>>>>>>> 95692e3411bc645b9759c857983409040074c80f
