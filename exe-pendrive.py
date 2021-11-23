from pendrive import Arquivo, penDrive


def main():
    sanDisk = penDrive("sanDisk")
    marl = penDrive("marl")
    fiel3 = Arquivo("juca", 4, 40)
    mar = Arquivo("mar", 1, 22000)
    sanDisk.Adicionar(fiel3)
    sanDisk.Adicionar(fiel3)
    sanDisk.Adicionar(Arquivo("mari", 2, 22))
    sanDisk.Adicionar(Arquivo("mar", 1, 22))
    sanDisk.Adicionar(Arquivo("maria", 3, 222002))
    sanDisk.Adicionar(Arquivo("mariana", 4, 22))
    print(sanDisk)
    sanDisk.Formatar()
    print(sanDisk)
    sanDisk.Adicionar(Arquivo("mar", 1, 22))
    sanDisk.Adicionar(Arquivo("maria", 3, 222002))
    sanDisk.Adicionar(Arquivo("mari", 2, 22))
    print(sanDisk)
    sanDisk.Copiar(fiel3, marl)
    sanDisk.Copiar(mar, marl)
    print(marl)
    marl.Mover(mar, sanDisk)
    print(sanDisk)
    print(marl)


if __name__ == "__main__":
    main()
