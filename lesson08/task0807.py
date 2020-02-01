# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex_number:

    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __str__(self):
        return f'{self.complex_num}'

    def __add__(self, other):
        return Complex_number(self.complex_num + other.complex_num)

    def __sub__(self, other):
        return Complex_number(self.complex_num - other.complex_num)

    def __mul__(self, other):
        return Complex_number(self.complex_num * other.complex_num)

    def __truediv__(self, other):
        return Complex_number(self.complex_num / other.complex_num)


cn1 = Complex_number(complex(1, 2))
cn2 = Complex_number(complex(2, 3))

print('Складываем')
print(cn1 + cn2)
print()
print('Вычитаем')
print(cn1 - cn2)
print()
print('Умножаем')
print(cn1 * cn2)
print()
print('Делим')
print(cn1 / cn2)
