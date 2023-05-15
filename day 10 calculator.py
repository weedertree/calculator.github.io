#calculator
#addition
def add(n1, n2):
    return n1+ n2
#subtraction
def sub(n1, n2):
    return n1-n2
#multiplication
def mult(n1, n2):
    return n1*n2
#divide
def divide(n1, n2):
    return n1/n2
    
#dictionary
operations ={ "+" : add ,
              "-" : sub ,
              "*" : mult ,
              "/" : divide ,
}

def calculator():
    print("""  _____________________
|  _________________  |
| | yoyo  calc 0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
 """)
    num1 = float(input("What is the first number?  \n"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("pick an operation from the line above :  ")
        num2 = float(input("What is the second Number? \n"))
        calculation_function = operations[operation_symbol]
        ans = calculation_function(num1, num2)
    
        print(f"{num1} {operation_symbol} {num2} = {ans}")
        
        
        if input((f"press 'y' to continue calculatin with {ans}, or type 'n' to stop ")) == "y":
           num1 = ans
        else:
            should_continue = False
            calculator()
        
calculator()
        