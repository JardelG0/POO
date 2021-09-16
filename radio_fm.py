def main():
    estações = {89.5: 'Cocais', 91.5:'Mix', 94.1:'Boa', 99.1:'Clube'}
    chaves = list(estações.keys())
    class RadioFM:
        def __init__(self, vol_max, estações):
            self.volume_min = 0
            self.volume_max = vol_max
            self.freq_min = 88
            self.freq_max = 108
            self.estações = estações
            self.volume = None
            self.ligado = False
            self.estação_atual = None
            self.frequencia_atual = None
            self.antena_habilitada = False

        def antena(self):
            if self.antena_habilitada == True:
                self.antena_habilitada = False
                print("Antena desabilitada!")
            else:
                self.antena_habilitada = True
                print("Antena habilitada!")

        def ligar(self):
            self.ligado = True
            self.volume = self.volume_min
            print("Rádio Ligado!")
            if self.antena_habilitada == True:
                self.frequencia_atual = chaves[0]
                self.estação_atual = self.estações[chaves[0]]
                print("Frequência {} -- Nome: {}".format( self.frequencia_atual, self.estação_atual))

        def desligar(self):
            self.ligado = False
            self.volume = None
            self.frequencia_atual = None
            self.estação_atual = None
            print("Radio desligado!")

        def aumentar_volume(self, aumentar = 1):
            if self.volume + aumentar < self.volume_max:
                self.volume += aumentar
                print("Volume:",self.volume)
            else:
                self.volume = self.volume_max
                print("Volume máximo!")

        def diminuir_volume(self, diminuir = 1):
            if self.volume - diminuir > self.volume_min:
                self.volume -= diminuir
                print("Volume:",self.volume)
            else:
                self.volume = self.volume_min
                print("Volume mínimo!")

        def mudar_frequencia(self, valor_freq = 0):
                if valor_freq:
                    self.frequencia_atual = valor_freq
                    if valor_freq in self.estações:
                        self.estação_atual = self.estações[valor_freq]
                        print("Frequência {} -- Nome: {}".format( self.frequencia_atual, self.estação_atual))
                    else:
                        self.estação_atual = "Estação inexistente"
                        print(self.estação_atual)
                else:
                    x = 0
                    for i in self.estações:
                        if self.frequencia_atual == i:
                            x += 1
                            if x == 4:
                                x = 0
                            break
                        else:
                            x += 1
                    self.frequencia_atual = chaves[x]
                    self.estação_atual = self.estações[chaves[x]]
                    print("Frequência {} -- Nome: {}".format( self.frequencia_atual, self.estação_atual))


    print("\t=== OBJETO 1 ===")
    rad_1 = RadioFM(15, estações)
    rad_1.antena()
    rad_1.ligar()
    rad_1.mudar_frequencia()
    rad_1.mudar_frequencia()
    rad_1.aumentar_volume(20)
    rad_1.diminuir_volume(4)
    rad_1.mudar_frequencia()
    rad_1.desligar()

    print("\n", 15 * "=-=", "\n")

    print("\t=== OBJETO 2 ===")
    rad_2 = RadioFM(20, estações)
    rad_2.antena()
    rad_2.ligar()
    rad_2.diminuir_volume(2)
    rad_2.mudar_frequencia(3)
    rad_2.mudar_frequencia(94.1)
    rad_2.aumentar_volume()
    rad_2.aumentar_volume()
    rad_2.aumentar_volume()
    rad_2.aumentar_volume(8)
    rad_2.desligar()

    print("\n", 15 * "=-=", "\n")

    print("\t=== OBJETO 3 ===")
    rad_3 = RadioFM(10, estações)
    rad_3.antena()
    rad_3.ligar()
    rad_3.aumentar_volume()
    rad_3.aumentar_volume(6)
    rad_3.aumentar_volume()
    rad_3.aumentar_volume()
    rad_3.mudar_frequencia()
    rad_3.mudar_frequencia(99.1)
    rad_3.diminuir_volume(2)
    rad_3.desligar()


if __name__ == "__main__":
    main()
