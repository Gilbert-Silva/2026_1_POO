class Data:
    def __init__(self, dia, mes, ano):
        self.set_data(f"{dia}/{mes}/{ano}")
#    def __init__(self, data):
#        self.set_data(data)
    def set_data(self, data):
        dia, mes, ano = map(int, data.split("/"))
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
        max_dia = 31
        if mes in [4, 6, 9, 11]: max_dia = 30
        if mes == 2:
            if bissexto: max_dia = 29
            else: max_dia = 28
        if 1 <= dia <= max_dia and 1 <= mes <= 12 and ano != 0:
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano
        else:
            raise ValueError("A data informada é inválida")         
    def get_dia(self): return self.__dia
    def get_mes(self): return self.__mes
    def get_ano(self): return self.__ano
    def __str__(self): return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano:04d}"

d = Data(31, 3, 2026)
print(d.get_dia())
print(d.get_mes())
print(d.get_ano())
print(d)


import datetime
d = datetime.date(2026, 3, 31)
print(d.strftime("%d/%m/%Y"))
