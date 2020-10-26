# Простой калькульятор
#################################################################################################
def main ():
    answer='д'
    while answer=='д' or answer=='Д':       # Цикл для вычисление
        operand1,operand2,operation=get_data()  # Получаем операнды
        result=calculate(operand1,operand2,operation)   # Вычисляем передавая в качестве аргумента операнды и оператор
        answer=input('Вы хотите работать над резултатом (д-да) : ')
        while answer=='д' or answer=='Д':       # Цикл если пользоваетль хочет продолжить работу
            try:                                # Улавливаем исключение
                operand1=result                 # Присваеваем резултат первому опреанду
                operand2 = float(input('Введите операнд 2 : '))
                operation = input('Выберите опреацию (+ - / * % ) : ')
                while operation.isalpha() or operation.isdigit():      # Валидация данных
                    print('Операция не может быть числом или буквой')
                    operation = input('Выберите опреацию (+ - / * % ) : ')

                result=calculate(operand1,operand2,operation)       # Вычисляем вызывая функцию
            except Exception as error:                              # Исключение
                print(error)
                exit()
            else:                   # Если не было вызвана исключение
                answer = input('Хотите продолжить работу над результатом ?(д-да) : ')
        if not answer=='д' or answer=='Д':
            answer=input('Вы хотите заново начать (д-да)?')

###############################################################################################
# В этой функции получаем данные от пользователья
def get_data():
    try:
        operand1=float(input('Введите операнд 1 : '))
        operand2=float(input('Введите операнд 2 : '))       # Получаем данные от пользователья
        operation=input('Выберите опреацию (+ - / * % ) : ')
        while operation.isalpha() or operation.isdigit():  # Валидация данных
            print('Операция не может быть числом или буквой')
            operation = input('Выберите опреацию (+ - / * % ) : ')

    except Exception as erorr:
        print(erorr)
        exit()
    else:       # Если исключений не было вызвана
        return operand1,operand2,operation

##############################################################################################
# Функция для вычисления
def calculate(op1,op2,operation):
    result=None
    try:
        if operation=='+':
            result=op1+op2
        elif operation=='-':
            result=op1-op2
        elif operation=='/':
            result=op1/op2      # Вычисляем в зависимости от оператора
        elif operation=='*':
            result=op1*op2
        elif operation=='%':
            result=op1%op2
    except Exception as error:
        print(error)
        exit()
    else:                       # Если исключений не было вызвана
        print(result)
        return result
###############################################################################################
main ()     # Выполняем программу