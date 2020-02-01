# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Warehouse:
    content = {}

    def __init__(self, name_wh):
        self.name_wh = name_wh

    def add_at_wh(self, office_equipment, count):
        try:
            count = int(count)
            if self.content.get(office_equipment.type_oe) is None:
                self.content[office_equipment.type_oe] = count
            else:
                self.content[office_equipment.type_oe] = self.content.get(office_equipment.type_oe) + count
            return self.content
        except ValueError:
            print('Количество может быть только числом')

    def del_from_wh(self, office_equipment, count):
        try:
            count = int(count)
            if self.content.get(office_equipment.type_oe) is None:
                return f'{office_equipment.name} на складе нет!'
            else:
                self.content[office_equipment.type_oe] = self.content.get(office_equipment.type_oe) - count
            return self.content
        except ValueError:
            print('Количество может быть только числом')


class Office_equipment:
    def __init__(self, maximum_format, weight, service_life, name, type_oe):
        self.name = name
        self.maximum_format = maximum_format
        self.weight = weight
        self.service_life = service_life
        self.type_oe = type_oe


class Printer(Office_equipment):
    def __init__(self, maximum_format, weight, service_life, name, print_speed):
        super().__init__(maximum_format, weight, service_life, name, 'printer')
        self.print_speed = print_speed


class Scanner(Office_equipment):
    def __init__(self, maximum_format, weight, service_life, name, scan_file_format):
        super().__init__(maximum_format, weight, service_life, name, 'scanner')
        self.scan_file_format = scan_file_format


class Copier(Office_equipment):
    def __init__(self, maximum_format, weight, service_life, name, copy_speed):
        super().__init__(maximum_format, weight, service_life, name, 'copier')
        self.copy_speed = copy_speed


wh1 = Warehouse('WH')
p1 = Printer('A4', '1 kg', '3 year', 'p1', '400 per sec')
wh1.add_at_wh(p1, 'ф')
s1 = Scanner('A4', '1 kg', '3 year', 's1', '100 per sec')
print(wh1.add_at_wh(p1, 40))
print(wh1.del_from_wh(p1, 3))
print(wh1.del_from_wh(s1, 3))
