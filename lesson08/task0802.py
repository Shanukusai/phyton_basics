# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = int(input('Enter the dividend: '))
    divider = int(input('Enter the divider: '))
    if divider == 0:
        raise OwnError("You cannot divide by 0!")
except ValueError:
    print("You entered not a number")
except OwnError as err:
    print(err)
else:
    print(f'{dividend} / {divider} = {dividend / divider}')
