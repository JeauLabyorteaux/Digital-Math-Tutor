from sympy import *

# One step linear equation solver
def one_step_linear():
x = symbols('x')

user_input = input("Enter your equation (e.g., x + 5 = 7): ")
if '=' not in user_input:
    print("Please make sure to include an '=' sign!")
else:
    lhs_str, rhs_str = user_input.split('=')


user = "x + 5 = 7".split('=')

lhs,rhs = sympify(user[0]), sympify(user[1])

op = lhs.func

if op == Add:
    print(op)
