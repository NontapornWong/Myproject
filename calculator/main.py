from logo import logo 
print(logo)

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    return a/b

operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

def calculator():
    num1 = float(input("What is the first number: "))
    for i in operator:
        print(i)

    loop = True
    while loop:
        ops_sym = float("Select operatior from the line above: ")
        num2 = float(input("What is the next number: "))
        function = operator[ops_sym]
        ans = function(num1, num2)

        print(f"{num1} {ops_sym} {num2} = {ans}")

        con_question = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit or type r to restart: ").lower()
        if con_question == "y":
            num1 = ans
        elif con_question == "n":
            loop = False
        elif con_question == "r":
            loop = False
            calculator()
calculator()

    


# loop = True
# while loop:
#     con_question = input(f"Type 'y' to continue calculating with {second_ans}, or type 'n' to exit: ").lower()
#     if con_question == "y":
#         ops_sym = input("Select another operation: ")
#         num4 = int(input("What is the next number: "))
#         function = operator[ops_sym]
#         third_ans = function(second_ans , num4)
#         print(f"{second_ans} {ops_sym} {num4} = {third_ans}")
#     elif con_question == "n":
#         loop = False