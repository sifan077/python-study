class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('wang wang')


class Cat(Animal):
    def speak(self):
        print('miao miao')


class Bird(Animal):
    def speak(self):
        print('chu chu')


def make_sound(animal):
    animal.speak()


if __name__ == '__main__':
    dog = Dog()
    make_sound(dog)
    cat = Cat()
    make_sound(cat)
    bird = Bird()
    make_sound(bird)
