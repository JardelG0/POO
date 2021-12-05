from datetime import date

class Banco:
    def __init__(self, nome):
        self.__nome=nome
        self.__contas=[]

    @property
    def nome(self):
        return self.__nome

    def Adicionar(self, conta):
        if type(conta) == Conta:
            self.__contas.append(conta)
            print("Conta de {} adicionada no banco {}".format(conta.titular.nome, self.nome))

    def Remover(self, conta):
        if conta in self.__contas:
            if conta.saldo == 0:
                self.__contas.remove(conta)
                print("Conta de {} foi removida do banco {}".format(conta.titular.nome, self.nome))
            else:
                print("A conta só pode ser removida se o saldo estiver zerado!")
        else:
            print("Conta não existente!")

    def valorTotal(self):
        soma = 0
        for i in range(len(self.__contas)):
            soma += self.__contas[i].saldo
        return soma

    def __str__(self):
        return "Banco: {} ==> Valor total depositado: ${}".format(self.nome, self.valorTotal())


class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo
    
    @property
    def titular(self):
        return self.__titular
    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, deposito):
        self.__saldo += deposito
        print(f'Depósito de ${deposito} efetuado!')

    def sacar(self, value):
        if self.__saldo - value >= 0:
            self.__saldo -= value
            print(f'Saque de ${value} efetuado!')
        else:
            print("Valor de saque indisponível!")
    
    def Pix(self, valor, conta):
        if type(conta) == Conta:
            if self.saldo >= valor:
                conta.__saldo += valor
                self.__saldo -= valor
                print(f'Pix de R${valor} realizado!')
            else:
                print("Sem saldo suficiente para realizar o pix!")
        else:
            print("Conta não indisponível")

    def pagar_boleto(self, boleto):
        if type(boleto) == Boleto:
            data_atual = str(date.today())
            data_vencimento = boleto.data_vencimento
            ano_atual = int(data_atual[:4])
            mes_atual = int(data_atual[5:7])
            dia_atual = int(data_atual[8:])
            ano_boleto = int(data_vencimento[6:])
            mes_boleto = int(data_vencimento[3:5])
            dia_boleto = int(data_vencimento[:2])
            def pagamento():
                if boleto.status != "pago":
                    if self.saldo >= boleto.valor:
                        self.__saldo -= boleto.valor
                        boleto.status = "pago"
                        print("Boleto de {} de R${} está {}!"\
                            .format(boleto.descricao, boleto.valor, boleto.status))
                    else:
                        print("Sem saldo suficiente para pagar o boleto!")
                else:
                    print("O boleto já está pago!")
            if ano_boleto == ano_atual:
                if mes_boleto == mes_atual:
                    if dia_boleto > dia_atual:
                        pagamento()
                    else:
                        print("Boleto vencido!")
                elif mes_boleto > mes_atual:
                    pagamento()
                else:
                    print("Boleto vencido!")
            elif ano_boleto > ano_atual:
                pagamento()
            else:
                print("Boleto vencido!")

    def __str__(self):
        return "Número: {} ==> Saldo: {}".format(self.numero, self.saldo)


class Cliente:
    def __init__(self, cpf, nome):
        self.__cpf=cpf
        self.__nome=nome

    @property
    def cpf(self):
        return self.__cpf
    @property
    def nome(self):
        return self.__nome
    
    def __str__(self):
        return "CPF: {} ==> Nome: {}".format(self.cpf, self.nome)

class Boleto:
    def __init__(self, codigo, descricao, data_venc, valor, status):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__data_vencimento = data_venc
        self.__valor = valor
        self.__status = status
    
    @property
    def data_vencimento(self):
        return self.__data_vencimento
    @property
    def valor(self):
        return self.__valor
    @property
    def descricao(self):
        return self.__descricao
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, value):
        self.__status=value
