# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self, type_wh, name):
        self.type = type_wh
        self.name = name


class Office_equipment:
    def __init__(self, maximum_format, dimensions, weight, service_life):
        self.maximum_format = maximum_format
        self.dimensions = dimensions
        self.weight = weight
        self.service_life = service_life


class Printer(Office_equipment):
    def __init__(self, print_speed):
        super().__init__(self)
        self.print_speed = print_speed


class Scanner(Office_equipment):
    def __init__(self, scan_file_format):
        super().__init__(self)
        self.scan_file_format = scan_file_format


class copier(Office_equipment):
    def __init__(self, copy_speed):
        super().__init__(self)
        self.copy_speed = copy_speed
