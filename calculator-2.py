def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def mod(a,b):
    return a % b
# storing values in dictionary format
operations_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
    "%":mod
}
# recursion- Function calling itself multiple time  By Using same variable (calculator()) three times
def calculator():
    number1=float(input("Enter a first Number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an Operation: ").lower()
        number2=float(input("Enter a next number: "))

        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculetion. or 'x' to exit : ").lower()
        if should_continue == 'y':
            number1=output
        elif should_continue == 'n':
            continue_flag=False
            calculator()
        else:
            should_continue =='x'
            continue_flag=False
            print("Exit Bye !")
calculator()