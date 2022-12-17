from fractions import Fraction
import cmath

def view_data(data):
    print(data)
    
def get_calc():
    n = int(input('Введите тип калькулятора: 1 - рациональные числа, 2 - комплексные числа: '))
    return n
    
def get_value_complex():
    n = int(input("Введите числитель: ")) 
    n1 = int(input("Введите знаменатель: "))    
    return(complex(n, n1))
    
def get_value_fract():
   n = int(input("Введите числитель: ")) 
   n1 = int(input("Введите знаменатель: "))    
   return(Fraction(n, n1))

def get_oper():
    oper = input("Введите оператор: ")
    return(oper)
