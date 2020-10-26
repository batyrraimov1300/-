# Эта программа показывет базовую цены на нефть
# и обрабатывает с помошью SMA (простой скользящей)
# и показывает оба графика для сравнения

import matplotlib.pyplot as plt  # Импортируем библиотеку из matplotlib модуль pyplot как plt


#########################################################################################################
# Функция main
def main():
    time_list, date, modified, standart = SMA()  # Получаем данные обработки и прочее
    plt.figure(figsize=(15, 7))
    plt.xlabel("Промежуток времени", fontsize='16', weight='bold')  # Ось X пишем описание
    plt.ylabel("Цены $", fontsize='16', weight='bold')  # ОСь Y пишем описание
    plt.title('Курс цен на фьючерсы нефти Brent', fontsize='16', weight='bold')  # Заголовок графика
    plt.xticks(time_list, date, fontsize=6, weight='bold')  # Ось X ставим дату
    plt.grid()  # Сетка

    plt.plot(time_list, modified, color='red', linestyle='solid', \
             label='SMA', marker='o')  # Строим SMA график
    plt.plot(time_list, standart, color='blue', linestyle='solid', \
             label='Стандартные значения', marker='>')  # Строим начальную график

    plt.legend(loc='upper right')  # Вставляем легенду

    plt.show()  # Отображаем график


###########################################################################################################
# Функция SMA обрабатывет начальные данные с
# помошью SMA и возвращает списки (начальную и обработанную)
def SMA():
    read = []  # Список чтобы читать данные из файла
    date = []  # Список которое будет содержать дату
    standart = []  # Стандартные значение цены
    modified = []  # Измененные значение цены будет записыватся
    i = 0  # Индексная переменная
    value=int(input('Введите количество итераций  : '))
    # Открываем файл в режиме чтения чтобы читать дату и курс нефти
    file = open('Oil.txt', 'r', encoding='utf-8-sig')

    for line in file:  # Читаем файл по строчно с поомошью цикла

        read.append(line.split())  # Добавляем списку read[] каждую дату и валюту
        # Даты и валюта будет добавлен как столбики то есть в двумерный список
        # Каждая строка это два столбика из даты и валюты

    file.close()  # Закрываем файл

    length = len(read)  # Присваимваем размер списка read на переменную length здесь len возвращает количество элементов
    while i < length:  # Открываем цикл используя длину списка read
        date.append(read[i][0])  # Присваиваем списку date только дату оcтавляя цену
        i += 1  # Индексная переменная

    i = 0  # Обновляем значение
    while i < length:  # Цикл не больше length итераций

        standart.append(read[i][1])  # Присваеваем на список standart только валюту из двумерного списка
        i += 1  # Считаем каждую строку

    standart = [float(x) for x in standart]  # Все строковые значение в списке standart конвертируем в float

    i = 0  # Индексная переменная
    while i < length:  # Цикл не больше length итераций
        calc=0
        while i < value:  # Цикл не больше value итераций
            modified.append(standart[i])  # Добавляем списку modified элементы standart[i]
            i += 1

        for y in range(value):          # Цикл откроем
            calc+=standart[i-y]         # Сложим все последнее value значений
        modified.append(calc/value)     # и добавляем в список с деленим на value
        i += 1

    time_list = list(range(0, length))  # time_list добавляем в спсиок в значение в диапазоне от 0 до 26
    return time_list, date, modified, standart  # Возвращаем данные


###############################################################################################################
main()  # Вызываем функцию main