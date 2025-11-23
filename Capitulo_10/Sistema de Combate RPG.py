import random

class Heroi:
    def __init__(self, nome, hp_maximo, forca):
        self.nome = nome
        self.hp_max = hp_maximo
        self.hp_atual = hp_maximo
        self.forca = forca
    def estar_vivo(self):
        return self.hp_atual > 0

    def atacar(self, inimigo):
        # Dano varia um pouco para dar emocao
        dano = self.forca + random.randint(-2, 2)
        print(f"{self.nome} ataca {inimigo.nome} causando {dano} de dano!")
        inimigo.receber_dano(dano)

    def receber_dano(self, dano):
        self.hp_atual -= dano
        if self.hp_atual < 0: self.hp_atual = 0
        print(f"{self.nome} ficou com {self.hp_atual}/{self.hp_max} HP.")

# Simulacao de Batalha
guerreiro = Heroi("Aragorn", 100, 15)
monstro = Heroi("Orc", 60, 10)

# O guerreiro ataca ate o monstro cair
while monstro.estar_vivo() and guerreiro.estar_vivo(): 
    guerreiro.atacar(monstro)
    if monstro.estar_vivo(): 
        monstro.atacar(guerreiro)
    print("---")

    if guerreiro.estar_vivo():
        print(f"Vitoria de {guerreiro.nome}!")
    else:
        print(f"{guerreiro.nome} caiu em combate...")
