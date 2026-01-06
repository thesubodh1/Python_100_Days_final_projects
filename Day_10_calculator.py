repeat = False
calculated_value = 0
flag = True

def calculate(number1,number2,symbol):
    if symbol == "+":
        return number1 + number2
    elif symbol == "-":
        return number1 - number2
    elif symbol == "*":
        return number1 * number2
    elif symbol == "/":
        return  number1 / number2
    else:
        return None

while flag:
    if not repeat:
        number_1 = float(input("what is the first number?: "))
        operator = input("Choose the operator: ")
        number_2 = float(input("what is the second number?: "))
        calculated_value = calculate(number_1,number_2,operator)
        print(f"{number_1} {operator} {number_2} = {calculated_value}")

    else:
        next_number = float(input("What is the next number: "))
        operator = input("Choose the operator: ")
        new_value = calculate(calculated_value,next_number,operator)
        print(f"{calculated_value} {operator} {next_number} = {new_value}")
        calculated_value = new_value


    want_to_repeat = input(f"Type 'y' to continue with {calculated_value} or 'n' to start new or 'exit' to quit: ").lower()
    if want_to_repeat == 'y':
        repeat = True
    elif want_to_repeat == 'n':
        repeat = False
        calculated_value = 0
    elif want_to_repeat == "exit":
        flag = False

