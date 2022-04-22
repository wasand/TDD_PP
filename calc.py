# TDD plus pair programming lab Andrzej Wąsik / Rafał Pawlędzio

class Calc(object):

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def int_max(num1, num2):
        return max(num1, num2)

    @staticmethod
    def int_min(num1, num2):
        return min(num1, num2)

    @staticmethod
    def is_positive(num2):
        if num2 > 0:
            return True
        else:
            return False

