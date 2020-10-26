import matplotlib.pyplot as plt


# Класс Average
class Average:
    def __init__(self,file): # Инициализация
        self.__file=file    # Имя файла
        self.__read=list()  # Пустой список


    def read(self):     # Метод read загружает данные из файла в оперативную память
        file=open(self.__file,'r',encoding="utf-8")     # Открыть файл в режиме чтения
        for line in file :  # Построчно читать файл
            self.__read.append(line.split())    # Добавить в список каждую строку как отдельный элемент
        file.close()    # Закрыть файл

    def sma(self):  # Метод средняя скользящая
        i=0
        standart=[] # Список изначальных значений
        modified=[] # Список значений после обоботки
        while True: # Цикл валидации данных

            value=int(input('Введите количество итераций(1-25) : '))
            if value<26 and value>0:    # Если было введено правильное значение
                break   # Выход из цикла

        length=len(self.__read) # Длина списка
        date=list()

        while i< length:    # Цикл сохраняет изначальные значение
            standart.append(self.__read[i][1])
            i += 1
        i=0 # Обновление переменного

        while i < length:  # Открываем цикл используя длину списка read
            date.append(self.__read[i][0])  # Присваиваем списку date только дату
            i += 1  # Операция инкремента

        standart=[float(x) for x in standart]   # Все строковые значение в числовую

        i=0 # Индексная переменная
        while i<length: # Цикл не больше length итераций
            calc=0
            while i<value:  # Цикл не больше value итераций
                modified.append(standart[i])    # Добавляем списку modified элементы standart[i]
                i+=1

            for y in range(value):  # Цикл откроем
                calc+=standart[i-y]      # Сложим все последнее value значений
            modified.append(calc/value)      # и добавляем в список с деленим на value
            i += 1

        time_list=list(range(0, length))        # time_list добавляем в спсиок в значение в диапазоне от 0 до 26

        return time_list, date, modified, standart

    def graph (self,time_list,date,modified,standart):
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


def main():
    MovingA=Average('Oil.txt')  # Создать обьект
    MovingA.read()  # Читать файл
    time_list, date, modified, standart=MovingA.sma()
    MovingA.graph(time_list,date,modified,standart) # Строит график

main()  # Выполнить программу