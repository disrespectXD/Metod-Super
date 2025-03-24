from asyncio import run_coroutine_threadsafe


class Tvarini:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        pass

    def info(self):
        return f'{self.name} йому {self.age} та він {self.color} кольору'

class Sobaka(Tvarini):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age, color)
        self.weight = weight

    def make_sound(self):
        return "РРРР...."

    def info(self):
        return super().info() + f", Вага {self.weight}"

class Kit(Tvarini):
    def __init__(self, name, age, color, yapping):
        super().__init__(name, age, color)
        self.yapping = yapping

    def make_sound(self):
        return "МЯЯЯЯЯЯЯУ"

    def info(self):
        return super().info() + f", Огризається: {'так' if self.yapping else 'Ні'}"


class Osoba():
    def __init__(self, name, years,):
        self.name = name
        self.years = years

    def get_age(self):
        return self.years

    def info(self):
        return f"Ім'я: {self.name} Вік: {self.years}"

class Vodila(Osoba):
    def __init__(self, name, years, license_number,):
        super().__init__(name, years)
        self.license_number = license_number

    def info(self):
        return super().info() + f", Номер: {self.license_number}"


class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Рухається зі швидкістю {self.speed} км/год"

class Car(Transport):
    def __init__(self, name, speed):
        super().__init__(speed)
        self.name = name

    def move(self):
         return f"Автомобіль {self.name} їде зі швидкістю {self.speed} км/год"

class Velik(Transport):
    def __init__(self, type, speed):
        super().__init__(speed)
        self.type = type

    def move(self):
        return  f"Велосипед {self.type} їде зі швидкістю {self.speed} км/год"
    
class Lodka(Transport):
    def __init__(self, name, speed):
        super().__init__(speed)
        self.name = name

    def move(self):
        return  f"Лодка {self.name} їде зі швидкістю {self.speed} км/год"


psina = Sobaka("Пес Дюк", 3, "чорного", "150кг")
kotik = Kit("Коксик", 2, "білого", True)
vodiy = Vodila("Іван", 35, "AB123456")
car = Car("BMW", 150)
velik = Velik("Україна", 25)
lodka = Lodka('Lamborghini', '120')

print(psina.info())
print(psina.make_sound())
print(kotik.info())
print(kotik.make_sound())
print(vodiy.info())
print(Car.move(car))
print(Velik.move(velik))
print(Lodka.move(lodka))