"""Postagem - 4
Classe Rádio:
estado (fixo com valor inicial = 'desligado')
volume (fixo com valor inicial  = 1)
faixa (AM/FM) 
frequencia_atual (fixo com valor = None)
"""

def main():
    class radio:
        modelo = None
        cor = None
        estado = None
        volume_max = 0
        volume_atual = 0
        mode_radio = None
        faixa_radio = None
        frequencia_atual = None
        mode_usb = None
        mode_aux = None
        mode_bluetooth = None

        def __init__(self):
            self.estado = "Desligado"
            self.volume = 1
            self.faixa_radio = "FM"
            self.frequencia_atual = None

        def ligar(self):
            if self.estado == "Desligado":
                self.estado = "Ligado"
                print("Rádio", self.estado)
            else:
                print("O rádio já está ligado")

        def desligar(self):
            if self.estado == "Ligado":
                self.estado = "Desligado"
                print("Rádio", self.estado)
            else:
                print("O rádio já está desligado")
        
        def frequencia(self, freq_atual):
            self.frequencia_atual = freq_atual
            print("FrenquÊncia:", self.frequencia_atual)

        def aument_vol(self, valor):
            if self.volume_atual + valor <= self.volume_max:
                self.volume_atual += valor
                print("Volume:", self.volume_atual) 
            else:
                self.volume_atual = self.volume_max
                print("Volume Máximo!")

        def dimin_vol(self, valor):
            if self.volume_atual - valor >= 0:
                self.volume_atual -= valor
                print("Volume:", self.volume_atual)
            else:
                self.volume_atual = 0
                print("Volume Mínimo!")

        def bluetooth(self):
            if self.mode_bluetooth == "Desligado":
                self.mode_aux = "Desligado"
                self.mode_usb = "Desligado"
                self.mode_radio = "Desligado"
                self.mode_bluetooth = "Ligado"
                print("Mode Bluetooth", self.mode_bluetooth)
            else:
                print("Modo Bluetooth já está ativo")

        def radio(self):
            if self.mode_radio == "Desligado":
                self.mode_aux = "Desligado"
                self.mode_usb = "Desligado"
                self.mode_bluetooth = "Desligado"
                self.mode_radio = "Ligado"
                print("Modo Rádio", self.mode_radio)
            else:
                print("Modo Rádio já está ativo")

        def faixa_r(self):
            if self.faixa_radio == "FM":
                self.faixa_radio = "AM"
                print("Faixa:", self.faixa_radio)
            else:
                self.faixa_radio = "FM"
                print("Faixa:", self.faixa_radio)

        def usb(self):
            if self.mode_usb == "Desligado":
                self.mode_aux = "Desligado"
                self.mode_radio = "Desligado"
                self.mode_bluetooth = "Desligado"
                self.mode_usb = "Ligado"
                print("Modo USB", self.mode_usb)
            else:
                print("Modo USB já está ativo")

        def aux(self):
            if self.mode_aux == "Desligado":
                self.mode_usb = "Desligado"
                self.mode_radio = "Desligado"
                self.mode_bluetooth = "Desligado"
                self.mode_aux = "Ligado"
                print("Modo AUX", self.mode_aux)
            else:
                print("Modo AUX já está ativo")


    # Objeto
    rad_1 = radio()
    rad_1.modelo = "Xtreme"
    rad_1.cor = "Azul"
    rad_1.estado = "Ligado"
    rad_1.volume_max = 20
    rad_1.volume_atual = 6
    rad_1.mode_radio = "Desligado"
    rad_1.mode_bluetooth = "Ligado"
    rad_1.mode_aux = "Desligado"
    rad_1.mode_usb = "Desligado"

    rad_2 = radio()
    rad_2.modelo = "Charge 2"
    rad_2.cor = "Preto"
    rad_2.estado = "Desligado"
    rad_2.volume_max = 15
    rad_2.volume_atual = 0
    rad_2.mode_radio = "Desligado"
    rad_2.mode_bluetooth = "Desligado"
    rad_2.mode_aux = "Desligado"
    rad_2.mode_usb = "Desligado"


    print("Modelo:",rad_1.modelo)
    print("Cor:",rad_1.cor)
    rad_1.bluetooth()
    rad_1.aument_vol(4)
    rad_1.radio()
    rad_1.aument_vol(12)
    rad_1.usb()
    rad_1.dimin_vol(23)
    rad_1.aument_vol(8)
    rad_1.ligar()
    rad_1.desligar()
    rad_1.faixa_r()
    rad_1.frequencia(4)


    print("\nModelo:",rad_2.modelo)
    print("Cor:",rad_2.cor)
    rad_2.desligar()
    rad_2.ligar()
    rad_2.radio()
    rad_2.aument_vol(7)
    rad_2.aument_vol(9)
    rad_2.aux()
    rad_2.dimin_vol(3)
    rad_2.desligar()


if __name__ == "__main__":
    main()
