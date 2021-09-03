"""Postagem - 4
Classe bicicleta:
velocidade_atual (fixo com valor inicial = 0)
veloc_maxima
altura_cela (fixo com valor inicial = 0)
altura_máxima 
calibragem_pneus (fixo com valor inicial = 0)
calibragem_max
tamanho_aro
"""

class Bicicleta:
    peso = None
    altura = None
    veloc_max = None
    veloc_atual = None
    cor = None
    aro = None
    alt_max_cela = None
    altura_cela = None
    calib_max_pneus = None
    calibragem_pneus = None


    def __init__(self, vel_max, alt_m_cela, alt_max, cal_max_pneus, aro):
        self.veloc_atual = 0
        self.veloc_max = vel_max
        self.altura_cela = 0
        self.alt_max_cela = alt_m_cela
        self.altura_máxima = alt_max
        self.calibragem_pneus = 0
        self.calib_max_pneus = cal_max_pneus
        self.aro = aro

    def pedalar(self):
        if self.veloc_atual < self.veloc_max:
            self.veloc_atual+=1
            print("Velocidade atual:",self.veloc_atual)
        else:
            print("Velocidade máxima!")

    def frear(self):
        if self.veloc_atual < 0:
            self.veloc_atual-=1
            print("Velocidade atual:",self.veloc_atual)
        else:
            print("Bicicleta parada!")

    def regular_cela(self, valor):
        if valor <= self.alt_max_cela:
            self.altura_cela = valor
            print("Altura atual da cela: {}cm".format(self.altura_cela))
        else:
            print("Altura máxima!")

    def calibrar_pneus(self, valor):
        if valor <= self.calib_max_pneus:
            self.calibrar_pneus = valor
            print("Calibragem atual dos pneus: {} libras".format(self.calibrar_pneus))
        else:
            print("Calibragem máxima!")


minha_bicicleta = Bicicleta(70, 20, 120, 20, 26)
minha_bicicleta.peso = 10
minha_bicicleta.altura = 100
minha_bicicleta.veloc_max = 60
minha_bicicleta.alt_max_cela = 25
minha_bicicleta.calib_max_pneus = 30
minha_bicicleta.cor = "Amarela"
minha_bicicleta.aro = 29
minha_bicicleta.regular_cela(5)
minha_bicicleta.calibrar_pneus(25)
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.frear()
minha_bicicleta.frear()
print("Cor:",minha_bicicleta.cor)
print("Aro:",minha_bicicleta.aro)

