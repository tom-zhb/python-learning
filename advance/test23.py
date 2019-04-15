#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习面向对象高级特性的多继承'

__author__ = 'sergiojune'


class Animal(object):
    pass


class Bird(Animal):
    def fly(self):
        print('fly------------Bird')
    pass


class Mammal(Animal):
    pass


# 加个扩展功能
class Flyable(object):
    def fly(self):
        print('fly------------Flyable')


class Runnable(object):
    def run(self):
        print("run---------Runnable")


# 这样就是多继承，加了和功能
class Dog(Mammal, Runnable):
    pass


# 多继承从左边往右继承，在父类中有相同的方法时就会先实现左边的方法，就近原则
class Parrot(Bird, Flyable):
    pass

s = Parrot()
s.fly()