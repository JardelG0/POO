def main():
    class BombaCombustível:
        def __init__(self, number, capac_bomb, qtd_combust, val_litro, type_combust = 1, val_faturado = 0, qtd_vendida = 0):
            self.__number = number
            self.__val_litro = val_litro
            self.__capac_bomb = capac_bomb
            self.__val_faturado = val_faturado
            self.__qtd_vendida = qtd_vendida
            self.__type_combust = type_combust
            if qtd_combust <= capac_bomb:
                self.__qtd_combust = qtd_combust
            else:
                self.__qtd_combust = capac_bomb

        def tipoCombustivel(self):
            if self.__type_combust == 1:
                self.__type_combust = "gasolina comum"
            elif self.__type_combust == 2:
                self.__type_combust = "gasolina aditivada"
            elif self.__type_combust == 3:
                self.__type_combust = "etanol"
            elif self.__type_combust == 4:
                self.__type_combust = "diesel"
        def abastecerBomba(self):
            if self.__qtd_combust <= self.__capac_bomb:
                self.__qtd_combust = self.__capac_bomb
                print("Bomba abastecida: {:.2f}L" .format(self.__qtd_combust))
        def abastecerVeiculoPorValor(self, value):
            combustivel = value/self.__val_litro
            if self.__qtd_combust - combustivel >= 0:
                self.__qtd_combust -= combustivel
                self.__qtd_vendida += combustivel
                self.__val_faturado += value
                print("Quantidade abastecida: {:.2f}L" .format(combustivel))
            else:
                print("Sem combustível suficiente!")
        def abastecerVeiculoPorLitro(self, value):
            if self.__qtd_combust - value >= 0:
                self.__qtd_combust -= value
                self.__qtd_vendida += value
                pagar = value * self.__val_litro
                self.__val_faturado += pagar
                print("Valor a ser pago: R${:.2f}" .format(pagar))
            else:
                print("Sem combustível suficiente!")

        @property
        def val_litro(self):
            return self.__val_litro 
        @val_litro.setter
        def val_litro(self,value):
            self.__val_litro=value
        @property
        def val_faturado(self):
            return self.__val_faturado
        def __str__(self):
            return f'Combustível na bomba: {self.__qtd_combust:.2f}L\nQuantidade vendida: {self.__qtd_vendida:.2f}L\nValor total faturado: R${self.__val_faturado:.2f}'

    bomb1 = BombaCombustível(1, 60, 50, 5.9, 1)
    bomb2 = BombaCombustível(2, 60, 60, 5.8, 2)
    bomb3 = BombaCombustível(3, 60, 40, 4.5, 3)
    bomb4 = BombaCombustível(4, 60, 48, 4.6, 4)

    bomb1.abastecerBomba()
    bomb1.abastecerVeiculoPorValor(40)
    bomb2.abastecerVeiculoPorLitro(15)
    bomb3.abastecerBomba()
    bomb3.abastecerVeiculoPorValor(150)
    bomb3.abastecerVeiculoPorLitro(30)
    bomb4.abastecerVeiculoPorValor(10)
    bomb4.abastecerVeiculoPorLitro(25)
    print("\n=== Resumo da Bomba 1 ===\n", bomb1)
    print("\n=== Resumo da Bomba 2 ===\n", bomb2)
    print("\n=== Resumo da Bomba 3 ===\n", bomb3)
    print("\n=== Resumo da Bomba 4 ===\n", bomb4)
    print("Arrecadação total do posto: R${:.2f}".format(bomb1.val_faturado+bomb2.val_faturado+bomb3.val_faturado+bomb4.val_faturado))


if __name__ == "__main__":
    main()
