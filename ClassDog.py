class Cachorro():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(self.nome.title() + " está sentado")

    def rolar(self):
        print(self.nome.title() + " esta rolando")