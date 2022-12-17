import modul_fract
import view
import logger 

def button_click():
    type_calc = view.get_calc()
    if type_calc == 1:        
        value_a = view.get_value_fract()
        value_b = view.get_value_fract()
    else:
        value_a = view.get_value_complex()
        value_b = view.get_value_complex()
    operator = view.get_oper()
    #modul_fract.init(value_a, value_b, operator)
    result = modul_fract.calc(value_a, value_b, operator)
    logger.operation_logger(value_a, value_b, operator, result)
    view.view_data(result)
    

