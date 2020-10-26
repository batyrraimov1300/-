# Импортируем стандартную библиотеку чтобы можно было запукать через терминал
import argparse

###################################################################################№
def main ():
    lists=get_data()    # Получаем данные от пользователья
    nums=numbers(lists) # Получаем список чисел
    print('Результат :',calculate(nums))    # Вывод результата

#####################################################################################
def get_data():         # Функция которая получает данные
    flag=True
    parser = argparse.ArgumentParser(description='Strings')
    parser.add_argument('-p', action='store', dest='count', type=str)
    args = parser.parse_args()  # Сделаем консольный ввод
    while flag:                 # Цикл нужен когда надо изменить способ ввода
        try:                    # Обрабатываем исключение
            flag=False
            string=(args.count) # Присваиваем переменную string консольные данные
                                # Если требуется изменить достаточно савить вместо args input () и удалить все что связан сним
            lists=list((string.split(','))) # Разделяем строку

            num=len(lists)
            if lists[num-1]=='':    # Разновидность валидации данных. Это нужен когда ставлен лишняя запятая в конце
                del lists[num-1]

            index =0
            while index<len(lists):     #  Обрабатываем список на правильность
                minus_number=lists[index]
                if not is_digit_minus(minus_number): # Вызываем функцию isdigit_minus()
                    flag=True
                index+=1
            if flag==True:
                print('Вы ввели неправильные данные !')
                exit()
            else:
                return lists
        except Exception as error : # Если было вызвано исключение
            print(error)
            exit()

############################################################################################
# Функция чтобы конвертировать строки
def numbers(nums):
    index= 0
    numbers=[]
    while index<len(nums):
        numbers.append(float(nums[index]))
        index+=1
    return numbers
###########################################################################################
# Функция вычиление
def calculate(lists):
    try:    # Обрабатываем исключение
            # Один из главных исключений деление на ноль
        i=0
        result=0
        while i<len(lists):
            result +=1/(lists[i]*2)
            i+=1
        return result
    except Exception as err:
        print(err)
        exit()
##########################################################################################
# Функция чтобы проверять принадлежность на численность
# в том числе отрицательные числа
def is_digit_minus(n):
    try:
        float(n)
        return  True
    except Exception :
        return False

##########################################################################################
main() # Выполняем программу