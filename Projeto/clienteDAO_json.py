from cliente import Cliente
import json

class ClienteDAO:
    def __init__(self):
        self.objetos = []
    def inserir(self, obj):
        self.abrir()
        # auto-incremento do id - calcula o maior id usado e soma um
        if len(self.objetos) == 0: id = 1
        else: id = (max(self.objetos, key = lambda x : x.id)).id + 1
        obj.id = id
        self.objetos.append(obj)
        self.salvar()
    def listar(self):
        self.abrir()
        self.objetos.sort(key = lambda x : x.nome)
        return self.objetos
    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.id == id: return obj
        return None        
    def atualizar(self, obj):
        # x é objeto que já está na lista com os dados desatualiazados e tem o 
        # mesmo id do novo objeto - obj
        x = self.listar_id(obj.id)
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()
    def excluir(self, obj):
        x = self.listar_id(obj.id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()
    def salvar(self):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)                 
    def abrir(self):
        self.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    self.objetos.append(c)        
        except FileNotFoundError:
            self.objetos = []
            
