from datetime import datetime as dt


def operation_logger(value_1, value_2, operator, result):
    time = dt.now().strftime('%H:%M')
    with open ('log.csv', 'a') as file:
        file.write('{}; value 1: {} value 2: {} operator: {} result: {}\n'
                   .format(time, value_1, value_2, operator, result))
