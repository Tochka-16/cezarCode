language = input('Привет! Выберите  язык (rus/eng): ')
text = list(input('Введите текст, которое хотите зашифровать: '))
key = int(input('Введите ключ (значение сдвига): '))

def cezarCode (language, text, key):
    res, var = [], ""

    if language == 'rus':
        lower, upper = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        N = 33

    elif language == 'eng':
        lower, upper = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        N = 25
    else:
        print('Такой опции нет!')

    for i in text:    
        if i in list(lower):
            var = list(lower)
        elif i in list(upper):
            var = list(upper)
        else:
            res.append(i)
        
        for i in var:
            for a in text:
                    if a == i:
                        try:
                            res.append(var[var.index(a) + key])
                        except IndexError:
                            index = key - (N - var.index(a))
                            res.append(var[index])

    cezarText = ''.join(res)
    print(cezarText)

cezarCode(language, text, key)