class Animal:
    def __init__(self, name: str, age: int, species: str) -> None:
        self.name = name
        self.age = age
        self._species = species
    def __str__(self) -> str:
        return f"{self.name} ({self._species}), {self.age} лет"
    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age}, species={self._species})"
    def make_sound(self) -> str:
        return "Some generic animal sound"
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age, species="Street dog")
        self.breed = breed
    def __str__(self) -> str:
        return f"{self.name} ({self.breed}), {self.age} лет"
    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"
    def make_sound(self) -> str:
        return "Gaf!"
    def fetch(self, item: str) -> str:
        return f"{self.name} принес(ла) {item}!"
if __name__ == "__main__":
    generic_animal = Animal("Бобик", 5, "Неизвестный вид")
    print(generic_animal)
    print(repr(generic_animal))
    print(generic_animal.make_sound())
    my_dog = Dog("Шарик", 3, "Лабрадор")
    print(my_dog)
    print(repr(my_dog))
    print(my_dog.make_sound())
    print(my_dog.fetch("мяч"))