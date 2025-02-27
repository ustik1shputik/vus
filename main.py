def main():
    array = []

    print("введите целые числа (максимум 15). Для завершения ввода введите 'stop':")

    while len(array) < 15:
        user_input = input(f"Введите число {len(array) + 1}: ")
        if user_input.lower() == 'stop':
            break
        try:
            number = int(user_input)
            array.append(number)
        except ValueError:
            print("введите целое число.")
    print("ваш массив:")
    print(array)


if __name__ == "__main__":
    main()
