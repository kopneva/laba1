numbers = ()
while True:
    user_input = input("Введите число (для завершения введите 'пробел'): ")
    if user_input == ' ':
        break
    elif not user_input.isdigit():
        print("Ошибка: введите только цифры")
    else:
        numbers += (int(user_input),)

if len(numbers) > 0:
    print("Первый элемент кортежа:", numbers[0])
    print("Последний элемент кортежа:", numbers[-1])
else:
    print("Кортеж пустой")