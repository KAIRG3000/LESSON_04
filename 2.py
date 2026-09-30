print("\nпрограмма запущена. что бы завершить програму введи - 0.")
while True:
    n = int(input("введите любое число - "))
    if n == 0:
        print("программа завершена")
        break
    k = 0
    s = 1
    while s * 2 <= n:
        s = s*2
        k = k + 1
    print( "\n", n, "\t", k, s, "\t2 **", k, "=", s)
    print()
