class ContaCorrente:
    def __init__(self, numero, saldo):
        self.__numero=numero
        self.__saldo=saldo

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    def creditar(self, value):
        self.__saldo += value
        print(f'O valor de R${value} foi creditado!')

    def debitar(self, value):
        if self.saldo >= value:
            self.__saldo -= value
            print(f'O valor de R${value} foi debitado!')
        else:
            print("Saldo insuficiente!")

    def transferir(self, value, conta):
        if type(conta) == ContaCorrente or ContaPoupança or ContaImposto:
            if self.saldo >= value:
                conta.__saldo += value
                self.__saldo -= value
                print("O valor de R${} foi transferido para a conta {}"\
                    .format(value, conta.__numero))
            else:
                print("Saldo insuficiente para essa transferência!")
        else:
            print("Conta indisponível!")
    
    def __str__(self):
        return "Número da conta: {} ==> Saldo: R${}"\
        .format(self.__numero, self.saldo)


class ContaPoupança(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.__taxa_juros = taxa_juros

    def renderJuros(self):
        self.saldo += self.saldo * self.__taxa_juros/100
        print("Os juros estão rendendo!")


class ContaImposto(ContaCorrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.__percentual_imposto = percentual_imposto

    def calcula_imposto(self):
        self.saldo -= self.saldo*self.__percentual_imposto/100
        print("Impostos calculados!")

