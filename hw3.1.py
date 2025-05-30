def calculator():
    while True:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, **, /, //, %) або 'exit' для виходу: ")

        if operator.lower() == 'exit':
            print("До побачення!")
            break

        num2 = float(input("Введіть друге число: "))

        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '**':
                result = num1 ** num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '//':
                result = num1 // num2
            elif operator == '%':
                result = num1 % num2
            else:
                print("Невідомий оператор")
                continue

            print("Результат:", result)

        except ZeroDivisionError:
            print("Помилка: Ділення на нуль недопустиме!")
        except ValueError:
            print("Помилка: Неправильний формат числа.")
        except Exception as e:
            print("Помилка:", str(e))

calculator()
