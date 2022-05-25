class FormulaError(Exception):
    def __init__(self, message="Formula Error"):
        self.message = message
        super().__init__(message)

def calc(x):
    x = x.split(" ")
    try:
         x[0] = float(x[0])
         x[2] = float(x[2])
    except ValueError:
        raise FormulaError
    if x[1] == "+":
        x = x[0] + x[2]
    elif x[1] == "-":
        x = x[0] - x[2]
    elif x[1] == "*":
        x = x[0] * x[2]
    elif x[1] == "/":
        x = x[0] / x[2]
    else:
        raise FormulaError
    return x
