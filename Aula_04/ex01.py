# Modelo
class Triangulo:
    def __init__(self):             # init - Define os atributos do objeto
        self.__b = 0
        self.__h = 0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError("Valor não pode ser negativo")
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Valor não pode ser negativo")
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):            # método que realiza uma operação com os dados do objeto
        return self.__b * self.__h / 2  

# Interface do Usuário - Visão
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
    @staticmethod
    def menu():
        print("1 - Triângulo, 9 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def triangulo():
        x = Triangulo()
        x.set_base(float(input("Informa a base do triângulo: ")))
        x.set_altura(float(input("Informa a altura: ")))
        print(f"A área do triângulo de base {x.get_base()} e altura {x.get_altura()} é {x.calc_area()}")

UI.main()
