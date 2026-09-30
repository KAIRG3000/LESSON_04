qua = 0
sum = 0
even = 0
odd = 0
max = 0
min = 0

print("Введите любое целое число")
while True:
    x = int(input("- "))
    if x == 0:
        break
    if qua == 0:
       max = x
       min = x
    else:
        if x > max:
            max = 9
            if x < min:
            min = x
    qua = qua + 1
    sum = x + sum
    if x % 2 == 0:
        even = even + 1
        odd = odd + 1
if qua > 0:
    mid = sum / qua
    print("\n введен ноль, программа окончена. вывод результата ")
    print(" подсчет... ")
    print("Количество:", qua)
    print("Сумма:", sum)
    print("Среднее арифметическое:", mid)
    print("Максимум:", max)
    print("Минимум:", min)
    print("Четных:", even)
    print("Нечетных:", odd)
else:
    print("введен 0")
