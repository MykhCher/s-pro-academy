class FormulaError(Exception):
    def __init__(self, message="Formula Error"):
        self.message = message
        super().__init__(message)

def calc(x):
    x = x.split(" ")
    if len(x) != 3:
        raise FormulaError("There are more/less than 3 items given")
    try:
         x[0] = float(x[0])
         x[2] = float(x[2])
    except ValueError:
        raise FormulaError("There are some non-number value given")
    if x[1] == "+":
        x = x[0] + x[2]
    elif x[1] == "-":
        x = x[0] - x[2]
    elif x[1] == "*":
        x = x[0] * x[2]
    elif x[1] == "/":
        try:
            x = x[0] / x[2]
        except ZeroDivisionError:
            x = "Cannot divide by zero"
    else:
        raise FormulaError("Unknown operation given, expected '+, -, *, /'")
    return x
