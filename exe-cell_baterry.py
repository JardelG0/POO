from cell_baterry import *

def main():
    bater_1 = Bateria(9532, 800, 80)
    bater_2 = Bateria(2395, 1000, 16)
    bater_3 = Bateria(3952, 1500, 100)
    Samsung = Celular(12345, bateria=bater_1)
    Nokia = Celular(54321, bateria=bater_2)
    Lg = Celular(14523, "Ligado", bater_3)

    Samsung.LigarDesligar()
    Samsung.retirarBateria()
    Samsung.colocarBateria(bater_1)
    Samsung.carregar(15)
    Nokia.assistirVideo(20)
    Nokia.LigarDesligar()
    Nokia.assistirVideo(15)
    Nokia.LigaDesligarWifi()
    Nokia.assistirVideo(10)
    Nokia.descarregar(10)
    Nokia.LigarDesligar()
    Lg.LigarDesligar()
    Lg.LigarDesligar()
    Lg.LigarDesligar()
    Lg.assistirVideo(16)
    Lg.descarregar(21)


if __name__ == "__main__":
    main()
