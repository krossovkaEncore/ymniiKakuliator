import math, time

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

g = {
    "moon": 2,
    "mars": 4,
    "earth": 10,
    "jupiter": 25
}

# Математический маятник
def matchPendulum():
    print("=== Математический маятник ===")
    
    planet = input("Выбери планету (moon, mars, earth, jupiter): ").lower()
    
    if planet not in g:
        print("Такой планеты нет.")
        return
    
    L = float(input("Введите длину маятника (в метрах): "))
    
    gravity = g[planet]
    
    T = 2 * math.pi * math.sqrt(L / gravity)
    v = 1 / T
    
    print("\nРезультаты:")
    print(f"Ускорение свободного падения: {gravity} м/с²")
    print(f"Период колебаний T = {T:.3f} секунд")
    print(f"Частота колебаний v = {v:.3f} Гц")
    print()


# Пружинный маятник
def springPendulum():
    print("=== Пружинный маятник ===")
    
    m = float(input("Введите массу груза (в кг): "))
    k = float(input("Введите жесткость пружины (Н/м): "))
    
    if k == 0:
        print("Жесткость не может быть равна 0.")
        return
    
    T = 2 * math.pi * math.sqrt(m / k)
    v = 1 / T
    
    print("\nРезультаты:")
    print(f"Период колебаний T = {T:.3f} секунд")
    print(f"Частота колебаний v = {v:.3f} Гц")
    print()

#  +===  Точка входа  ===+
if __name__ == "__main__":
    while True:
        try:
            num = int(input(
                "Здравствуйте, я типо умный калькулятор и усе такое выберете что вам нужно:\n"
                "0) Выход\n"
                "1) Обычный калькулятор\n"
                "2) I = q / t\n"
                "3) R = q * (e / S)\n"
                "4) математический маятник\n"
                "5) пружинный маятник\n"
                "\nВведите номер функции: "
            ))
            if num == 0:
                exit()
            elif num == 1:
                calculator()
                time.sleep(1)
            elif num == 2:
                Iqt()
                time.sleep(1)
            elif num == 3:
                Rqes()
                time.sleep(1)
            elif num == 4:
                matchPendulum()
                time.sleep(1)
            elif num == 5:
                springPendulum()
                time.sleep(1)
            else:
                print("Неверный ввод!")
        except ValueError:
            print("Неверный ввод!")
        except Exception as e:
            print(f"Произошла ошибка: {e}") 