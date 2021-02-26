
# Создаем простой класс собака
class Dog:

    # Задаем специальный метод, который автоматически выполняется при создании каждого нового экземпляра
    def __init__(self, name, age): # Конструктор класса, "магический метод"
        # Инициализируем атрибуты name и age
        self.name = name
        self.age = age

    def sit(self):
    # Собака садится по команде
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
    # Собака перекатывается по команде
        print(self.name.title() + " rolled over!")


# my_dog = Dog('willy', 6)
dog_input_name = input("Введите кличку собаки: ").lower()
dog_input_age = input("Введите возраст собаки: ")
my_dog = Dog(dog_input_name, dog_input_age)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()