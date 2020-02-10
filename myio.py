

#string

phrase = input("Enter a string: ")
print("You said: " + phrase)
print(f" You said {phrase}")

#float
somefloat = float(input("Enter a Float: "))
print("You entered float: " + str(somefloat))
print(f"You erntered float: {somefloat}")

#int
someint = float(input("Enter an int: "))
print("You entered int: " + str(someint))
print(f"You entered int: {someint}")

#string interpolation
print(f"Do python inline, like this: {somefloat} * {someint} = {somefloat * someint}")
