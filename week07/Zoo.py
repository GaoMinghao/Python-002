# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 5:23 PM
# @Author  : minghao.gao
# @FileName: Zoo.py
# @Software: PyCharm
class Zoo(object):
    animal_id_set = set()

    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        if not issubclass(animal.__class__, Animal):
            return
        class_name = type(animal).__name__
        if id(animal) not in self.animal_id_set:
            self.animal_id_set.add(id(animal))
            setattr(self, class_name, class_name)


class Animal(object):
    def __new__(cls, *args, **kwargs):
        if cls is Animal:
            raise TypeError("Animal can not be instantiated.")
        return object.__new__(cls)

    def __init__(self, category, size, temper):
        self.category = category
        self.size = size
        self.temper = temper

    @property
    def is_feral(self):
        if (self.size == '中' or self.size == '大') and self.category == '食肉' and self.temper == '凶猛':
            return True
        return False


class Cat(Animal):
    sound = '喵'

    def __init__(self, name, category, size, temper):
        self.name = name
        super().__init__(category, size, temper)

    @property
    def is_petty(self):
        if self.temper == '凶猛':
            return False
        return True


class Dog(Animal):
    sound = '汪'

    def __init__(self, name, category, size, temper):
        self.name = name
        super().__init__(category, size, temper)

    @property
    def is_petty(self):
        if self.temper == '凶猛':
            return False
        return True


if __name__ == '__main__':
    z = Zoo('时间动物园')
    cat1 = Cat('猫 1', '食肉', '小', '温顺')
    dog1 = Dog('狗', '食肉', '大', '凶猛')

    print(cat1.is_petty)
    print(cat1.is_feral)
    have_cat = hasattr(z, 'Cat')
    have_dog = hasattr(z, 'Dog')
    print(have_cat)
    print(have_dog)

    z.add_animal(cat1)
    z.add_animal(dog1)
    have_cat = hasattr(z, 'Cat')
    have_dog = hasattr(z, 'Dog')
    print(have_cat)
    print(have_dog)
    print(Zoo.animal_id_set)

    cat2 = Cat('猫 2', '吃草', '大', '温顺')
    z.add_animal(cat2)
    z.add_animal(cat1)
    print(Zoo.animal_id_set)
