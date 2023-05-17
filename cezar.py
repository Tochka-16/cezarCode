language = input('Привет! Выберите  язык (rus/eng): ')
text = list(input('Введите текст, которое хотите зашифровать: '))
key = input('Введите ключ (значение сдвига): ')


def cezarCode ():
    res = []
    
    if language == 'rus':
        RUS_ALPHABET_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        RUS_ALPHABET_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        N = 33

        for i in text:
            
            if i == i.lower():
                for a in list(RUS_ALPHABET_lower):
                    if i == a:
                        try:
                            res.append(list(RUS_ALPHABET_lower)[list(RUS_ALPHABET_lower).index(a) + int(key)])
                        except IndexError:
                            index = int(key) - (N - list(RUS_ALPHABET_lower).index(a))
                            res.append(list(RUS_ALPHABET_lower)[index])
                                       
            elif i == i.upper():
                for b in list(RUS_ALPHABET_upper):
                    if i == b:
                        try:
                            res.append(list(RUS_ALPHABET_upper)[list(RUS_ALPHABET_upper).index(b) + int(key)])
                        except IndexError:
                            index = int(key) - (N - list(RUS_ALPHABET_upper).index(b))
                            res.append(list(RUS_ALPHABET_upper)[index])

            elif i not in list(RUS_ALPHABET_lower) and list(RUS_ALPHABET_upper):
                res.append(i)               

    elif language == 'eng':
        ENG_ALPHABET_lower = 'abcdefghijklmnopqrstuvwxyz'
        ENG_ALPHABET_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        N = 25

        for i in text:
            
            if i == i.lower():
                for a in list(ENG_ALPHABET_lower):
                    if i == a:
                        try:
                            res.append(list(ENG_ALPHABET_lower)[list(ENG_ALPHABET_lower).index(a) + int(key)])
                        except IndexError:
                            index = int(key) - (N - list(ENG_ALPHABET_lower).index(a))
                            res.append(list(ENG_ALPHABET_lower)[index])

            elif i == i.upper():
                for b in list(ENG_ALPHABET_upper):
                    if i == b:
                        try:
                            res.append(list(ENG_ALPHABET_upper)[list(ENG_ALPHABET_upper).index(b) + int(key)])
                        except IndexError:
                            index = int(key) - (N - list(ENG_ALPHABET_upper).index(b))
                            res.append(list(ENG_ALPHABET_upper)[index])

            elif i not in list(RUS_ALPHABET_lower) and list(ENG_ALPHABET_upper):
                res.append(i) 
            
    else:
        print ('Шифрование на этом языке отсутствует :( )')
        return 2/0
    

    cezarText = ''.join(res)
    print(cezarText)  

