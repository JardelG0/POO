from Bank import Banco, Cliente, Conta, Boleto

def main():
    conta1 = Conta(54345, Cliente(76123423, "Juca"))
    conta2 = Conta(65735, Cliente(76123423, "Juca"), 243)
    conta3 = Conta(76980, Cliente(76123423, "Juca"), 500)
    conta4 = Conta(80703, Cliente(23454534, "Paula"), 300)
    conta5 = Conta(23923, Cliente(63452321, "Peter"), 440)
    conta6 = Conta(98123, Cliente(63452321, "Peter"), 560)
    Boleto1 = Boleto(888888, "Conta de luz", "16/01/2022", 73, "não pago")
    Boleto2 = Boleto(444444, "Conta de água", "03/12/2021", 94, "não pago")
    Boleto3 = Boleto(222245, "Fatura do Cartão", "22/03/2022", 140, "pago")
    Boleto4 = Boleto(222245, "Eletrodoméstico na casas bahia", "22/03/2022", 140, "não pago")

    Bradesco = Banco("Bradesco")
    Caixa = Banco("Caixa")
    Inter = Banco("Inter")

    Bradesco.Adicionar(conta1)
    conta1.sacar(20)
    conta1.depositar(50)
    Caixa.Adicionar(conta2)
    conta2.sacar(243)
    Caixa.Remover(conta2)
    Inter.Adicionar(conta3)
    Inter.Remover(conta3)
    Inter.Remover(conta4)
    Caixa.Adicionar(conta5)
    conta5.sacar(70)
    Caixa.Adicionar(conta6)
    conta6.depositar(203)
    conta6.pagar_boleto(Boleto1)
    conta2.pagar_boleto(Boleto3)
    conta5.pagar_boleto(Boleto2)
    conta1.pagar_boleto(Boleto1)
    conta1.pagar_boleto(Boleto4)
    conta4.Pix(40, conta3)
    conta4.Pix(300, conta5)

    print(Bradesco)
    print(Caixa)
    print(Inter)


if __name__ == "__main__":
    main()
