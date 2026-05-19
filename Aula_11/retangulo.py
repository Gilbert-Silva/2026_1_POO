class Retangulo:
    def __init__(self, b, h):
        self.__b = b
        self.__h = h
    def calc_area(self):
        return self.__b * self.__h 
    def calc_diagonal(self):
        return (self.__b **2 + self.__h ** 2) ** 0.5 
    def __str__(self):
        return f"Retângulo com base = {self.__b} e altura = {self.__h}"
       