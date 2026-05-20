import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.id = id         # atributo de instância
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
    def get_id(self) : return self.id    
    def get_nome(self) : return self.nome    
    def get_email(self) : return self.email    
    def get_fone(self) : return self.fone    
    def get_senha(self) : return self.senha    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
