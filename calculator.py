from scipy.integrate import quad
a = int(input("first_number> "))
b = int(input("second_number> "))
function = input("sum, sub, mul, div, power, Int> ")
def calculator(a,b):
    if function == "sum":
        print(a+b)
    elif function == "sub":
        print(a-b)
    elif function == "div":
        print(a/b)
    elif function == "mul":
        print(a*b)
    elif function == "power":
        print(a**b)
    elif function=="Int":
        I = quad(integrand, 0, 1, args=(a,b))
        print(I)
    else:
        print("we dont have this feature enabled")

def integrand(x, a, b):
    return a*x**2 + b

calculator(a,b)



   