import MathFunctions as mf
# from math import *
import math

if __name__ == '__main__':
    # list = [1, 3, 5, 7, 9]
    # for element in list:
    #     print(element * 2)
    #
    # string = "Prochka"
    # for character in string:
    #     print(character)
    #
    # list = [(1, "Eden"), (2, "Dva"), (3, "Tri")]
    # for (x, y) in list:
    #     print(f'{x} {y}')
    #
    # rangeList = range(3, 14, 5)
    #
    # for element in rangeList:
    #     print(element)
    #
    # rangeListNegative = range(10, 2, -1)
    # for e in rangeListNegative:
    #     print(e)
    #
    #
    # fruits = ["banana","apple","mango"]
    # print(len(fruits))
    # for index in range(len(fruits)):
    #     print(f'{index}: {fruits[index]}')

    # ages = {"Dimitrija": 21, "Branka": 56, "Tomislav": 64}
    #
    # for name in ages.keys():
    #     print(f'{name}: {ages[name]} години')
    #     print(name)

    # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # # Земи ги парните елементи и помножи ги со 10.
    # list2 = [element * 10 for element in list if element % 2 == 0]
    # print(list2)
    #
    # print(mf.najdiPlostinaNaKrug(5))
    #
    # print(math.sqrt(2))
    #
    #
    # class Plant:
    #     def __init__(self, type):
    #         self.type = type
    #
    #     def get_type(self):
    #         return self.type
    #
    #
    # class Flower(Plant):
    #     def __init__(self, color, type):
    #         super().__init__(type)
    #         self.color = color
    #         self.type = type
    #
    #     def get_color(self):
    #         return self.color
    #
    #
    #
    # x = Flower("Lila", "Afrikanska Ljubichica")
    # y = Flower("Roze", "Sardela")
    #
    # print(y.get_age())

    def swap(a, b):
        tmp = a
        a = b
        b = tmp
        return a, b


    listStart = [('a', 1), ('b', 2), ('c', 3)]

    # listEnd = [swap(a, b) for (a, b) in listStart]
    listEnd = [(b, a) for (a, b) in listStart]

    print(listEnd)
