# Дыма Владимир. КНИТ16-А
# Алгоритм Кнута-Морриса-Пратта

import numpy as np

S = input('Введите строку: ')
W = input('Введите искомую подстроку: ')

# Создадим странную, но полезную таблицу.
# Эта таблица показывает где начинать искать совпадения, если прошлый раз
# не нашли всю подстроку.
T = np.arange(0, len(W))  # Генерируем таблицу в длину подстроки.
T[0] = -1  # Обозначим первый элемент как -1, чтобы потом получалась
           # "фигня" и не пришлось делать лишних действий.
T[1] = 0  # Ну а тут нолик, чтобы не повторяться с первым. Сейчас поймете.
pos = 2  # Из-за прошлых двух товарищей начинаем со 2 позиции.
cnd = 0  # Ну типа начало.
while pos < len(W):  # Тут тоже, вроде, понятно.
    if W[pos-1] == W[cnd]:  # Есди окажется что у нас вначале и где-нибудь
        cnd += 1  # ещё в подстроке есть одинаковые последовательности символов,
        T[pos] = cnd  # то мы все это дело отметим, чтобы потом учитывать это
        pos += 1  # во время поиска.
# Таким образом таблица будет примерно такая:
#  ABCDABD -  ABC -> ABD
# -1000012 - -100 -> 012
# Если мы видим, что в подстроке есть символ, похожий на первый символ
# подстроки, то мы начинаем это все дело запоминать(повторяюсь). Но почему
# отмечаем его за ноль, если нулем мы отмечаем чуть ли не все остальное?
# Потому что. Позже мы будем отнимать T[i] элемент, и чтобы не отнимать больше,
# чем нужно, нумеруем с нуля, иначе придется выполнять лишние действия.
    elif cnd > 0:  # Это для чего-то сверхсложного. Простите, не понял.
        cnd = T[cnd]  # И вам не советую. НЕ ЛЕЗЬ!
    else:
        T[pos] = 0  # Заполним нулями все, что не совпадает.
        pos += 1

# Это основной алгоритм проверки.
m = 0  # Текущая позиция в строке S, совпадающая с началом W
i = 0  # Позиция в искомой строке W
while m+i < len(S):  # Если сумма этих двух внезапно превысит размер S, то
                     # все потеряно.
    if W[i] == S[m+i]:  # Тут мы просто сравниваем симолы W и S.
        if i == len(W)-1:  # Если i примет занчение длины W - 1, то это
                           # успех!
            print('Успех! Подстрока найдена на позиции {}.'.format(m))
            exit()  # И уходим.
        i += 1  # Прибавим к i единичку, если совпали символы.
    else:  # А если не совпало что-то, то переходим к интересной части.
        if T[i] > -1:  # Если у нас i элемент в Т больше -1, то значит, что
                       # значит, что где-то в проверке было начало подстроки
            m += i - T[i]  # тогда мы устанавливаем m на место, где был провал,
            i = T[i]  # а i на позицию, после начальных элементов.
                      #  СЛОЖНА!
        else:
            m += 1  # А если вообще фигня какая-то, то просто пойдем дальше.
            i = 0  # Ну тут всё ясно.
else:
    print('Провал! Подстрока не найдена.')
