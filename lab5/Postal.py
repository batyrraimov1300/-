import  matplotlib.pyplot as plt

def main ():
    dictionary=get_mail_dict('mbox.txt')   # Получаем словарь
    name=[]
    messages=[]
    space=[]

    for n,m in dictionary.items():  # Сортируем по отдельности ключь и значение
        name.append(n)
        messages.append(m)
    hist_names=space+name

    Conf_Spam,names_dsp=X_DSPAM_Conf(name)    # Выясняем спамеров по параметру Conf передавая полученные адреса
                                                # и получаем адреса которые не смог обнаружить параметр Confidence
    date_sp=Date(names_dsp)     # Отправляем эти адреса на обработку по времени отправки
    date_sp.update(Conf_Spam)   # Похожие адреса удаляем оставляя одного
    for y,x in enumerate(date_sp):  # Вывод с нумерацией адресов спамеров
        print(y+1,' ',x,'/////спамер')
    histogramm(messages,hist_names)

######################################################################################

# В этой функции получам эл.адреса и количество писем
def get_mail_dict(filepath):
    f = open(filepath)
    lines = f.readlines()   # Присваиваем весь файл в один список
    d = {}                  # Открываем словарь
    for line in lines:      # Читаем список
        line_splitted = line.split(' ')  # Разделяем строку на списки

        if line_splitted[0] == 'From':  # Если 0 элемент равно From 1 элемент будет имя автора
                                            # Поэтому ниже проверяем есть ли этот ключь в словаре
            if line_splitted[1] in d.keys():    # Если второй элемент есть в словаре
                d[line_splitted[1]] += 1        # Увеличиваем значение этого клча на единицу так мы будем считать письма
            else:
                d[line_splitted[1]] = 1         # Иначе добавить в список со значением 1

    f.close()   # Закрываем файл
    return d    # Возвращаем словарь
###############################################################################################3

# Функция для проверки спамеров по Confidence
def X_DSPAM_Conf (name):

    spammers=[]             # Список для спамеров
    file=open('mbox.txt','r',encoding='utf-8')
    for x in file : # Читаем файл
        y=x
        if 'X-DSPAM-Confidence' in x :  # Если встречаем параметр
            i=0
            while i<5:
                x=file.readline()
                i+=1
                if 'Author:' in x:      # Если встречаем эл.адрес
                    for n in name:
                        if n in x :     # Выясняем какой именно
                            s=y.split() # Разделяем параметр
                            lengthh=len(s)  # Количество элементов
                            value=float(s[lengthh-1])   # Получаем значение параметра

                            if value>0.99:              # Если больше этого он заносится в список спамеров
                                spammers.append(n)
                                num=name.index(n)       # Выясняем индекс
                                del name[num]           # Удаляем имя из списка чтобы повторно не проверять

    return spammers,name    # Отправляем имена

# Спамеры по дате отправки
def Date(name):
    file =open('mbox.txt','r')
    lists=[]
    for x in file:  # Читаем файл
        if 'Author:' in x : # Находим адрес
            i=0
            while i<len(name):  # Читаем адресов по одному

                if  name[i] in x:   # Если есть совпадение
                    lists.append(x) # Добавляем имя в список
                    x=file.readline()  # Читем дату отправки
                    y=x.split(':')      # Разделяем дату
                    lists.append(y[1])  # Получаем только год месяч день и час
                i+=1
    spam_name=[]
    for n in name:  # Читаем имена
        date = []
        i=0
        while i<len(lists):
            if n in lists[i]:   # Если имя в списке
                date.append(lists[i+1]) # Добавляем толко время сообщений одного эл.адреса
                # Анализ дат
                for el in date: # Читаем новый созданный список только из дат одного  автора

                        j=0
                        total=0
                        while j<len(date):
                            if el==date[j]: # Сравниваем между собой
                                total+=1
                                if total>5 :    # Если будеть больше пяти одинаковых дат
                                    spam_name.append(n)     # Добавляем в список спамеров
                            j+=1
            i+=1
    sets=set()  # Создаем множество чтобы удалить одни и те же адреса
    sets.update(spam_name)  # Присвваиваем список спамеров в множества
    return sets     # Вернем как результат
####################################################################################################
#   Строим Гистограмму
def histogramm (messages,name):

    plt.figure(figsize=(12,6))
    left_edges=[0]*46       # Создаем ось X
    i=0                     # Индексная переменная
    for x in range (3,141,3):    # Заполняем список
        left_edges[i]=x
        i+=1
    heights= [] # Ось y
    for x in messages:
        heights.append(x)

    y_tick =[]
    for yt in range (0,205,5):
        y_tick.append(yt)
    s_ytick=[]                  # Настройка меток деления y
    for yt in y_tick:
        ys=str(yt)
        s_ytick.append(ys)
    plt.yticks(y_tick,s_ytick,fontsize=8)

    xtick=[]
    for num in range(3,141,3):
       xtick.append(num)
    s_xtick=[]                      # Настройка меток деления x
    for x in range (1,47):
        s_xtick.append(x)
    plt.xticks(xtick,s_xtick,fontsize=9)

    plt.title('Гистограмма по отправителям')    # Заголовок
    plt.xlabel('Отправители')                   # Отправители на оси X
    plt.ylabel('Количество Писем')              # Количество писемь на оси Y

    print('Электронные почты по номеру на Гистограмме')
    print('--------------------------------------')
    for i, x in enumerate(name):
        print(i + 1, '\t', '--------', x)

    plt.bar(left_edges,heights,1)     # Создаем гистограмму
    plt.show()                      # Выводим гистограмму на экран

################################################################################################3
main()