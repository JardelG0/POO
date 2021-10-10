def main():
    class Pessoa:
        def __init__(self, nome, idade, peso, altura, sexo, estado="vivo", estado_civil="solteiro", conjugue=None):
            self.__nome = nome
            self.__idade = idade
            self.__peso = peso
            self.__altura = altura
            self.__sexo = sexo
            self.__estado = estado
            self.__estado_civil = estado_civil
            self.__conjugue = conjugue


        def envelhecer(self):
            if self.__estado == "vivo":
                self.__idade += 1
                if self.__idade < 21:
                    self.__altura += 5
                print(f'{self.__nome} está com {self.__idade} anos e {self.__altura}cm de altura.')
            else:
                print(self.__nome,"está morto(a)")

        @property
        def idade(self):
            if self.__estado == "vivo":
                print(self.__idade)
            else:
                print(self.__nome,"está morto(a)")
        @idade.setter
        def idade(self, value):
            print("Sem permissão")
        @property
        def estado_civil(self):
            return self.__estado_civil
        @estado_civil.setter
        def estado_civil(self, value):
            self.__estado_civil = value

        def engordar(self, gain_kilos=1):
            if self.__estado == "vivo":
                self.__peso += gain_kilos
                print(f'{self.__nome} engordou {gain_kilos}kg e agora está com {self.__peso}kg')
            else:
                print(f'Operação não realizada. {self.__nome} está {self.__estado}')
                
        def emagrecer(self, lose_kilos):
            if self.__estado == "vivo":
                self.__peso -= lose_kilos
                print(f'{self.__nome} emagreceu {lose_kilos}kg e agora está com {self.__peso}kg')
            else:
                print(f'Operação não realizada. {self.__nome} está {self.__estado}')

        def crescer(self, height):
            if self.__estado == "vivo":
                if self.__idade <= 21:
                    self.__altura += height
                else:
                    print(f'{self.__nome} não pode mais crescer pois está com 21 anos ou mais')
            else:
                print("VOCÊ ESTÁ MORTO!")

        def casar(self, conjugue):
            if type(conjugue) == Pessoa:
                if self.__estado == "vivo" and conjugue.__estado == "vivo":
                    if self.__nome != conjugue.__nome:
                        if self.__idade >= 18 and self.__estado_civil != "casado(a)" and conjugue.__idade >= 18 and conjugue.__estado_civil != "casado(a)":
                            self.__estado_civil = "casado(a)"
                            conjugue.__estado_civil = "casado(a)"
                            self.__conjugue = conjugue
                            conjugue.__conjugue = self
                            print(f'{self.__nome} está casado com {conjugue.__nome}.')
                        else:
                            if self.__idade < 18:
                                print(f'Casamento não permitido. {self.__nome} é de menor.')
                            elif conjugue.__idade < 18:
                                print(f'Casamento não permitido. {conjugue.__nome} é de menor.')
                            elif self.__estado_civil == "casado(a)":
                                print(f'Casamento não realizado. {self.__nome} é {self.__estado_civil}.')
                            elif conjugue.estado_civil == "casado(a)":
                                print(f'Casamento não realizado. {conjugue.__nome} é {conjugue.__estado_civil}.')
                    else:
                        print("Não é permitido carsar-se consigo mesmo(a)!")
                else:
                    if self.__estado == "morto":
                        print(f'Casamento não realizado. {self.__nome} está morto(a)')
                    elif conjugue.__estado == "morto(a)":
                        print(f'Casamento não realizado. {conjugue.__nome} está morto(a)')
            else:
                print("Casamento não realizado! O conjugue deve ser uma pessoa")

        def divorciar(self, conjugue):
            if self.__estado and conjugue.__estado == "vivo":
                if self.__conjugue == conjugue:
                    self.__estado_civil = "divorciado(a)"
                    conjugue.__estado_civil = "divorciado(a)"
                    print(f'{self.__nome} está {self.__estado_civil} de {conjugue.__nome}')
                else:
                    print("Você só pode se divorciar do seu conjugue!")
            else:
                print("Os dois precisam estar vivos para se divorciarem!")

        def morrer(self):
            self.__estado = "morto(a)"
            print(f'{self.__nome} morreu.')
            if self.__estado_civil == "casado(a)":
                self.__conjugue.__estado_civil = "viúvo(a)"
                print(f'E agora {self.__conjugue.__nome} está {self.__conjugue.__estado_civil}')


    maria = Pessoa("Maria", 5, 20, 100, "F")
    joão = Pessoa("João", 12, 40, 140, "M")
    pedro = Pessoa("Pedro", 22, 65, 170, "M")
    bia = Pessoa("Bia", 18, 55, 160, "F")
    julia = Pessoa("Julia", 30, 65, 170, "F")
    cadu = Pessoa("Carlos", 2, 11, 80, "M")
    jonas = Pessoa("Jonas", 34, 70, 180, "M")

    maria.idade = 10
    maria.envelhecer()
    pedro.crescer(2)
    pedro.engordar(3)
    bia.casar(cadu)
    pedro.casar(maria)
    pedro.casar(julia)
    pedro.casar(bia)
    maria.morrer()
    maria.engordar()
    bia.casar(jonas)
    bia.divorciar(jonas)
    print(jonas.estado_civil)
    bia.morrer()
    pedro.morrer()
    jonas.casar(julia)
    julia.emagrecer(2)
    pedro.casar(bia)
    pedro.idade
    joão.idade = 50


if __name__ == "__main__":
    main()
