
import arty


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {       # عندما نريد فقط التخزين لا نكتب أقواس الوظائف، بل نكتبها دون أقواس، لأن الأقواس للاستدعاء
    "+": add,        # هنا نخزن علامة + في الوظيفة add
    "-": subtract,   # هنا نخزن علامة - في الوظيفة subtract
    "*": multiply,   # هنا نخزن علامة * في الوظيفة multiply
    "/": divide,     # هنا نخزن علامة / في الوظيفة divide
}                    # عندما نستدعي أي مفتاح ستأتي معه العملية الحسابية؛ لأني ربطت المفتاح بالوظيفة في القاموس

# print(operations["*"](4, 8))


def calculator():
    print(arty.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)   # هنا عندما أدخلت المتغير operation_symbol وما فيه مربوط بإحدى الوظائف فيلزم تعبئة n1 و n2 التي في الوظائف من هنا
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 100)
            calculator()


calculator()
