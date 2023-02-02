def main(Number_One):
    global Number_First
    Action_Choise = input("Выберите: 1) Умножить 2) Поделить 3) Сложить 4) Вычесть 5) Возвести в степень 6) Обнулить:\n")
    Sum = float()
    match Action_Choise:
        case "1":
            Sum = mul(Number_One, float(input("Введите число: ")))
            print("Результат: ", Sum)
        case "2":
            Sum = div(Number_One, float(input("Введите число: ")), Number_First)
            print("Результат: ", Sum)
        case "3":
            Sum = add(Number_One, float(input("Введите число: ")))
            print("Результат: ", Sum)
        case "4":
            Sum = sub(Number_One, float(input("Введите число: ")))
            print("Результат: ", Sum)
        case "5":
            Sum = deg(Number_One, float(input("Введите число: ")))
            print("Результат: ", Sum)
        case "6":
            zeroing()
            main(Number_First)
    Number_First = Sum

def mul(First_Number, Second_Number):
    Sum = float(First_Number * Second_Number)
    return Sum

def div(First_Number, Second_Number, Summ):
    if Second_Number != 0:
        Sum = float(First_Number / Second_Number)
        return Sum
    else:
        print ("На ноль делить нельзя")
        Sum = Summ
        return Sum

def add(First_Number, Second_Number):
    Sum = float(First_Number + Second_Number)
    return Sum

def sub(First_Number, Second_Number):
    Sum = float(First_Number - Second_Number)
    return Sum

def deg(First_Number, Second_Number):
    Sum = float(First_Number ** Second_Number)
    return Sum

def zeroing():
    global Number_First
    Number_First = float(input("Введите число: "))
    return Number_First

zeroing()

while True:
    main(Number_First)