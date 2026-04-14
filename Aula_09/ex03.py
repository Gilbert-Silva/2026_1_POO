import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

def salvar():
    a = Cliente(1, "Douglas Crockford")
    b = Cliente(2, "Jon Bosak")
    lista = [a, b]
    with open("clientes.json", mode="w") as arquivo:
        json.dump(lista, arquivo, default = vars)   
    #arquivo = open("clientes.json", mode="w")
    #json.dump(lista, arquivo, default = vars)
    #arquivo.close()

def abrir():
    lista = []
    with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
            c = Cliente(obj["id"], obj["nome"])
            lista.append(c)
    for c in lista: print(c)

#salvar()
abrir()




