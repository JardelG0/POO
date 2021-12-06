from contas import *

def main():
    conta1 = ContaCorrente(12432, 50)
    conta2 = ContaCorrente(43215, 0)
    conta3 = ContaPoupança(42342, 0, 5)
    conta4 = ContaPoupança(99283, 170, 10)
    conta5 = ContaImposto(52312, 500, 25)
    conta6 = ContaImposto(33333, 439, 8)

    conta1.creditar(70)
    conta2.transferir(500, conta3)
    conta2.debitar(2)
    conta1.transferir(20, conta2)
    conta3.renderJuros()
    conta3.debitar(80)
    conta4.renderJuros()
    conta5.calcula_imposto()
    conta5.debitar(200)
    conta6.calcula_imposto()
    conta6.creditar(11)

    print(conta1)
    print(conta2)
    print(conta3)
    print(conta4)
    print(conta5)
    print(conta6)


if __name__ == "__main__":
    main()
 