import math
import re
def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = gcd_extended(b % a, a)
    return (div, y - (b // a) * x, x)

a = input("введите выражение: ")
pattern = r"[()]|[*/]|[+-]|\d+"
z = 0
while z < 999:
    z += 1
    result = re.findall(pattern, a)
    massive_a = a.split()
    if len(result) == len(massive_a):
        break
    else:
            a = input("неправильное выражение, попробуйте ещё раз")
massive_a = a.split()

b = int(input("Введите поле: "))
u = 0
while u < 999:
    u += 1
    o = 0
    for i in range(2, b // 2+1):
        if (b % i == 0):
            o +=1
    if (o <= 0):
        break
    else:
        b = int(input("Нужно простое число для поля"))

i = 0
j = 0
if '/' not in massive_a:  #есть ли в списке деление
    j += 0
else:
    j += 1
if j > 0: #если есть
    AllindexList = []
    print(massive_a, "массив введенной строки")
    for index, value in enumerate(massive_a):
        if list((index, value))[1] == '/':
            AllindexList.append(list((index, value))[0])
    print(AllindexList, 'идексы деления')

    indexList = []
    i = 0
    while i < len(AllindexList):
        print(massive_a[int(AllindexList[i]) - 1])
        if massive_a[int(AllindexList[i]) - 1] == '1':
            indexList.append(AllindexList[i])
        i += 1
    print(indexList, "индексы для евклида")

    g = 0
    newNumber = []
    while g < len(indexList):
        a1 = int(massive_a[indexList[g]+1])
        print(gcd_extended(a1,b), "вывод x,y,b")
        newNumber.append(gcd_extended(a1,b)[1])
        g += 1
    r = 0
    print(massive_a, "до")
    print(newNumber, "массив решенных по евклиду выражений которые нужно вставить в исходный массив")
    print(len(indexList),"range листа индексов для евклида")
    q = 0
    p = 0
    if len(indexList) != 0:

        while q <= len(indexList):
            massive_a[indexList[q]-p] = newNumber[q]
            print(massive_a, "A")
            massive_a.pop(indexList[q] - p - 1) # вставляю в массив решенную дробь в виде числа
            print(massive_a, "B")
            massive_a.pop(indexList[q] - p)
            print(massive_a, "C")
            p = p + 2
            q += 1
            if q == len(indexList):
                break

        a_mew = "".join(map(str, massive_a))
        print(a_mew, "вывод нового массива в виде строки")
        a2 = eval(a_mew)
        print(a2 % b, "= x")
        print(massive_a, "после")


    else:  # если нет
        a1 = eval(a)  # просто ищем остаток
        print(a1 % b, "=x")
else: #если нет
    a1 = eval(a) #просто ищем остаток
    print(a1 % b, "=x")
