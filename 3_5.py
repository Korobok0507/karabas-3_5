# Создание функции
def get_multiplied_digits(number):

    # Преобразование число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Первая цифра в числовом формате
        first = int(str_number[0])
        # Умножение с рекурсивным вызовом функции (приводит к
        # последовательной разбивке числа на цифры с
        # последующим умножением начиная с последней цифры)
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Возвращаем единственную цифру
        return int(str_number)

# Ввод числа от пользователя
user_input = int(input("Введите число: "))
result = get_multiplied_digits(user_input)
print("Произведение цифр:", result)