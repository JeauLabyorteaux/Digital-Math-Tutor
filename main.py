from sympy import *

x = Symbol('x')

safe_dict = {'x': x}

def get_user_equation() -> Tuple[Expr, Expr]:
    
    # Loop until we get a clean equation from the user
    while True:

        # Gather user input

        user_input = input("Enter your equation: ")
        
        if not user_input:
            print("Please make sure to enter an equation!")
            continue
        elif '=' not in user_input:
            print("Please make sure to include an '=' sign!")
            continue
        else:
            try:
                lhs_str, rhs_str = user_input.split('=')
            except Exception:
                print("Please enter a valid input! (Only 1 '=')")
                continue
            


        # Convert to SymPy objects safely

        try:
            lhs = parse_expr(lhs_str, local_dict=safe_dict)
            rhs = parse_expr(rhs_str, local_dict=safe_dict)
        except Exception:
            print("Please enter a valid equation!")
            continue


        # Check for subscripting

        symbol_names = [s.name for s in (lhs - rhs).free_symbols]
        
        has_subscript = any(name.startswith('x') and name != 'x' for name in symbol_names)
        
        if has_subscript:
            print("Error: Subscripts (like x2 or x₂) are not supported.")
            continue
        
        # Check that it can be solved

        sol = solve(Eq(lhs,rhs))

        if not sol:
            print("This problem does not have a solution!")
            continue 
        else:
            return lhs, rhs

    

    


# One step linear equation solver
def one_step_linear(lhs, rhs):

    # Check to make sure this is a linear equation
    if degree(lhs-rhs,x) > 1:
        pprint(Eq(lhs,rhs))
        print("This is not a linear function")
        return 

    print("Let's solve!")

    pprint(Eq(lhs,rhs))

    # Set a max_steps just in case while loop never exits
    steps = 0

    # Solved is defined as lhs = x
    
    while lhs != x:
        
        # Emergency Exit
        if steps > 20:
            print("Too many steps. Error Occured. Exiting...")
            break

        steps += 1
        
        # If variable exists on the right side
        if rhs.has(x):

            x_term = rhs.coeff(x) * x

            # Subtration Property of Equality
            lhs -= x_term
            rhs -= x_term

            print(f"Subtract {x_term} from both sides to isolate x on left hand side.x2=4")

            continue

        # If constant on left side
        constant, _ = lhs.as_coeff_Add()
        if constant != 0:

            # Subtraction Property of Equality
            lhs -= constant
            rhs -= constant

            print(f"Subtract {constant} from both sides to move constants to right hand side.")

            continue

        # If variable has coefficient
        coefficient, _ = lhs.as_coeff_mul(x)
        if coefficient != 1:

            # Division Property of Equality
            lhs /= coefficient
            rhs /= coefficient

            print(f"Divide {coefficient} from both sides to isolate x on left hand side.")

            continue

    if steps <= 20:
        print("Solved!")
        pprint(Eq(lhs,rhs))
    return


        
if __name__ == '__main__':

    left_side, right_side = get_user_equation()

    one_step_linear(left_side, right_side)

