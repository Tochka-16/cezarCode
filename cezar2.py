language = input('Привет! Выберите  язык (rus/eng): ')
text = input('Введите текст, который хотите зашифровать: ')
key = int(input('Введите ключ (значение сдвига): '))

def cezarCode (language, text, key):
    res = []
    
    if language == 'rus':
        simbol = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') 
        N = 33
    elif language == 'eng':
        simbol = list('abcdefghijklmnopqrstuvwxyz')
        N = 25
    else:
        print('Такой опции нет!')
        exit()

    for index in range(len(text)):

        if text[index] in simbol:

            for lit in simbol:
                if lit == text[index] and (simbol.index(lit) + key) / N < 1:
                    res.append(simbol[simbol.index(lit) + key])
                elif lit == text[index] and (simbol.index(lit) + key) / N > 1:
                    t = key - (N - simbol.index(lit))
                    res.append(simbol[t])

        elif text[index] in ''.join(simbol).upper():

            for lit in simbol:
                if lit.upper() == text[index] and (simbol.index(lit) + key) / N < 1:
                    res.append(simbol[simbol.index(lit) + key].upper())
                elif lit.upper() == text[index] and (simbol.index(lit) + key) / N > 1:
                    t = key - (N - simbol.index(lit))
                    res.append(simbol[t].upper())

        else: 
            res.append(text[index])

    cezarText = ''.join(res)
    print(cezarText)

cezarCode(language, text, key)
