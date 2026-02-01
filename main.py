# +=== Обычный калькулятор ===+
def calculator():
    print("\n === Это обычный калькулятор, чтобы выйти введите exit. === \n")
    while True:
        try:
            fun = input(">>> ")
            if fun != "exit":
                print(f'Ответ: {eval(fun)}')
            else:
                break
        except:
            print("\n === Ошибка, вы ввели что-то помимо цифр и операторов. === \n")


def Iqt():
    """
    сила тока(I) = заряд(q) / время(t)
    заряд(q) = сила тока(I) * время(t)
    время(t) = заряд(q) / сила тока(I)
    """
    print("\n=== Формула I = q / t ===")
    print("Что нужно найти?")
    print("1) Сила тока (I)")
    print("2) Заряд (q)")
    print("3) Время (t)")

    choice = int(input("Введите номер: "))

    if choice == 1:
        q = float(input("Введите заряд q (Кл): "))
        t = float(input("Введите время t (с): "))
        I = q / t
        print(f"\nСила тока I = {I} А")

    elif choice == 2:
        I = float(input("Введите силу тока I (А): "))
        t = float(input("Введите время t (с): "))
        q = I * t
        print(f"\nЗаряд q = {q} Кл")

    elif choice == 3:
        q = float(input("Введите заряд q (Кл): "))
        I = float(input("Введите силу тока I (А): "))
        t = q / I
        print(f"\nВремя t = {t} с")

    else:
        print("Неверный выбор!")


def Rqes():
    """
    R = q * (e / S)
    """
    print("\n=== Формула R = q * (e / S) ===")
    print("Что нужно найти?")
    print("1) Сопротивление (R)")
    print("2) Плотность материала (q)")
    print("3) Сечение проводника (S)")
    print("4) Длина провода (e)")

    choice = int(input("Введите номер: "))

    if choice == 1:
        q = float(input("Введите плотность материала q: "))
        e = float(input("Введите длину провода e: "))
        S = float(input("Введите сечение S: "))
        R = q * (e / S)
        print(f"\nСопротивление R = {R} Ом")

    elif choice == 2:
        R = float(input("Введите сопротивление R (Ом): "))
        S = float(input("Введите сечение S: "))
        e = float(input("Введите длину провода e: "))
        q = (R * S) / e
        print(f"\nПлотность материала q = {q}")

    elif choice == 3:
        q = float(input("Введите плотность материала q: "))
        e = float(input("Введите длину провода e: "))
        R = float(input("Введите сопротивление R (Ом): "))
        S = q * (e / R)
        print(f"\nСечение проводника S = {S}")

    elif choice == 4:
        R = float(input("Введите сопротивление R (Ом): "))
        S = float(input("Введите сечение S: "))
        q = float(input("Введите плотность материала q: "))
        e = (R * S) / q
        print(f"\nДлина провода e = {e}")

    else:
        print("Неверный выбор!")


#  +===  Точка входа  ===+
if __name__ == "__main__":
    num = int(input(
        "Здравствуйте, я типо умный калькулятор и усе такое выберете что вам нужно:\n"
        "1) Обычный калькулятор\n"
        "2) I = q / t\n"
        "3) R = q * (e / S)\n"
        "\nВведите номер функции: "
    ))
    if num == 1:
        calculator()
    elif num == 2:
        Iqt()
    elif num == 3:
        Rqes()