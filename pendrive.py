from _typeshed import Self


class penDrive:
    def __init__(self, nome):
        self.__nome=nome
        self.__tamanho=64*1000
        self.__arquivos=[]

    property
    def nome(self):
        return self.__nome
    property
    def tamanho(self):
        return self.__tamanho

    def Adicionar(self, file):
        if type(file) == Arquivo:
            temp = None
            for i in self.__arquivos:
                if file.nome == i.nome:
                    temp = True
            if temp:
                print("Alert! Já existe um arquivo com o mesmo nome")
            else:
                if file.tamanho <= self.VerificaEspaçoLivre():
                    self.__arquivos.append(file)
                    print("Arquivo adicionado")
                else:
                    print("Espaço insuficiente!")
        else:
            print("Arquivo não compatível")

    def Remover(self, file):
        if file in self.__arquivos:
            self.__arquivos.remove(file)
            print("Arquivo excluído!")
        else:
            print("Arquivo não encontrado!")

    def VerificaEspaçoLivre(self):
        espac_usado=0
        if self.__arquivos != []:
            for i in self.__arquivos:
                espac_usado += i.tamanho
            if self.__tamanho - espac_usado >= 0:
                return self.__tamanho - espac_usado
            else:
                return 0
        else:
            return self.__tamanho

    def Formatar(self):
        self.__arquivos = []
        print("Dispositivo formatado!")

    def Copiar(self, file, penD):
        if type(file) == Arquivo:
            if type(penD) == penDrive:
                for i in self.__arquivos:
                    if file.nome == i.nome:
                        penD.Adicionar(file)
                        print("Arquivo copiado!")
                    else:
                        print("Arquivo não encontrado!")
            else:
                print("Dispositivo não reconhecido!")
        else:
            print("Arquivo não reconhecido!")


    def Mover(self, file, penD):
        if type(file) == Arquivo:
            if type(penD) == penDrive:
                for i in self.__arquivos:
                    if file.nome == i.nome:
                        penD.Adicionar(file)
                        print("Arquivo movido!")
                        self.Remover(file)
                    else:
                        print("Arquivo não encontrado!")
            else:
                print("Dispositivo não reconhecido!")
        else:
            print("Arquivo não reconhecido!")


    def __str__(self):
        if len(self.__arquivos) > 1:
            for i in range(len(self.__arquivos)):
                if i == 0:
                    print("PenDrive {} com {}GB:\n{}".format\
                        (self.__nome, self.__tamanho/1000, self.__arquivos[i]))
                elif i != len(self.__arquivos)-1 and i != 0:
                    print(self.__arquivos[i])
                elif i == len(self.__arquivos)-1:
                    return "{}\n{:.1f}% ocupado".format(self.__arquivos[i],(self.__tamanho - self.VerificaEspaçoLivre()) * 100/self.__tamanho)
        elif len(self.__arquivos) == 1:
            return "PenDrive {} com {}GB:\n{}\n{:.1f}% ocupado".format\
                (self.__nome, self.__tamanho/1000, self.__arquivos[0], (self.__tamanho - self.VerificaEspaçoLivre()) * 100/self.__tamanho)
        else:
            return "PenDrive {} com {}GB:\n{}\n{}% ocupado".format\
                (self.__nome, self.__tamanho/1000, "Sem arquivos!", 0)

#Adicionar, Remover, VerificaEspaçoLivre, Formatar, Copiar, Mover

class Arquivo:
    def __init__(self, nome, tipo, tamanho):
        self.__nome=nome
        if tipo == 1:self.__tipo=".txt"
        elif tipo == 2:self.__tipo=".img"
        elif tipo == 3:self.__tipo=".mp4"
        elif tipo == 4:self.__tipo=".exe"
        self.__tamanho=tamanho

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, name):
        self.__nome = name
    @property
    def tipo(self):
        return self.__tipo
    @property
    def tamanho(self):
        return self.__tamanho
    if Self.__tipo == ".txt":
        @tamanho.setter
        def tamanho(self, taman):
            self = taman
    else:
        print("Formato de arquivo não alterável!")
    def __str__(self):
        return "Arquivo {}{} de {}MB".format(self.__nome, self.__tipo, self.__tamanho)

# espaço * 100/64