from fractions import Fraction 

x = 0
y = 0
#w = 0
#z = 0
operator = ''

def init(a, b, c, d, operat):
    global x
    global y
    #global w
    #global z
    global operator
    x = Fraction(a, b) 
    y = Fraction(c, d)
    operator = operat
    
def calc(x, y, operator):    
    if operator == '+':
        return(x + y)
    elif operator == '-':
        return(x - y)
    elif operator == '*':
        return(x * y)
    elif operator == '/':
        return(x / y)

