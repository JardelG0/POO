class Bateria:
    def __init__(self, codigo, capacidade, percentual_carga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentual_carga = percentual_carga
    
    @property
    def percentual_carga(self):
        return self.__percentual_carga
    @percentual_carga.setter
    def percentual_carga(self, valor):
        self.__percentual_carga=valor

    def carregar(self, valor):
        if type(valor) == int and self.__percentual_carga + valor <= 100:
            self.__percentual_carga += valor
            print("Celular carregado: {}%".format(self.__percentual_carga))
        else:
            print("Alert! Valor inválido ou excedente")
    def descarregar(self, valor):
        if type(valor) == int and self.__percentual_carga - valor >= 0:
            self.__percentual_carga -= valor
            print("Celular descarregado: {}%".format(self.__percentual_carga))
        else:
            print("Alert! Valor inválido ou excedente")


class Celular:
    def __init__(self, mei, wifi="Desligado", bateria=None):
        self.__mei = mei
        self.__bateria = bateria
        self.__wifi = wifi
        self.__ligado = False

    def LigarDesligar(self):
        if self.__ligado == True:
            self.__ligado = False
            print("Celular Desligado!")
        else:
            if self.__bateria == None:
                print("Alert! Celular sem bateria")
            elif self.__bateria.percentual_carga == 0:
                print("Alert! Celular está descarregado")
            else:
                self.__ligado = True
                print("Celular Ligado! ==> Carga da bateria: {}%".format(self.__bateria.percentual_carga))
    def colocarBateria(self, bateria):
        if self.__bateria != None:
            print("Alert! O celular já possui uma bateria")
        else:
            if type(bateria) == Bateria:
                self.__bateria = bateria
                print("Bateria colocada")
    def retirarBateria(self):
        if self.__bateria != None:
            self.__bateria = None
            print("Bateria retirada")
        else:
            print("O celular já está sem bateria")
    def LigaDesligarWifi(self):
        if self.__ligado == True:
            if self.__wifi == "Desligado":
                self.__wifi = "Ligado"
                print("Wifi ligado!")
            else:
                self.__wifi = "Desligado"
                print("Wifi desligado!")
        else:
            print("Alert! O celular está desligado")
    def assistirVideo(self, tempo):
        if self.__ligado == True:
            if self.__wifi == "Ligado":
                gasto_bat = tempo * 5
                if self.__bateria.percentual_carga - gasto_bat > 0:
                    self.__bateria.percentual_carga -= gasto_bat
                    print("Reprodução completa!")
                else:
                    print("Alert! Sem carga suficiente para assistir!")
            else:
                print("Alert! O wifi precisa estar ativado")
        else:
            print("Alert! O celular precisa estar ligado")
    def carregar(self, valor):
        self.__bateria.carregar(valor)
    def descarregar(self, valor):
        self.__bateria.descarregar(valor)
