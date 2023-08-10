import abc
class conta(abc.ABC):
    def __init__(self,agencia,conta, saldo):
        self.agencia= agencia
        self.conta= conta
        self.saldo= saldo 

    @abc.abstractmethod
    def sacar(self,valor):...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'[DEPOSITO]{valor}')

    def detalhes(self,msg=''):

        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')

class CPoupanca(conta):
    def sacar(self, valor):
        valor_sacado = self.saldo - valor

        if valor_sacado >=0:
            self.saldo -= valor
            self.detalhes(f'sacado {valor} ')
            return self.saldo
        
        print('Não é possivel saca valor desejado!')
        self.detalhes(f'Saque negado{valor}')


class CCorente(conta):
      def __init__(self,agencia,conta, saldo,limite):
        super().__init__ (agencia,conta, saldo)
        self.limite= limite

      def sacar(self, valor):
        valor_sacado = self.saldo - valor

        if valor_sacado >=0:
            self.saldo -= valor
            self.detalhes(f'sacado {valor} ')
            return self.saldo
        
        print('Não é possivel saca valor desejado!')
        print(f'Seu limite é {-self.saldo:.2f}')
        self.detalhes(f'Saque negado{valor}')



if __name__ =='__main__': # texta o codigo no modulo  e quando importa para main ele não seja execultado 
      cpopanca1 = CPoupanca(111, 222)
      cpopanca1.sacar(1)
      cpopanca1.depositar(10)
      cpopanca1.sacar(2)
      cpopanca1.sacar(9)
      print('******')
      print('\n')
      CCorente1 = CCorente(111, 222,0, 100)
      CCorente1.sacar(1)
      CCorente1.sacar(1)
      CCorente1.depositar(10)
      CCorente1.sacar(2)
      CCorente1.sacar(9)

      
