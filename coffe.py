class Beverage():

    def cost(self) -> float:
        pass


class Espresso(Beverage):

    def cost(self) -> float:
        return 60

class  HouseBlend(Beverage):

    def cost(self) -> float:
        return 60



class Condiments(Beverage):

    _beverage: Beverage = 0

    def __init__(self, beverage: Beverage) :
        self._beverage = beverage

    @property
    def beverage(self) -> Beverage:
   

        return self._beverage

    def cost(self) -> float:
        return self._beverage.cost()

class Mocha(Condiments):

    def cost(self) -> float:
        return self.beverage.cost() + 15 


def run(beverage: Beverage) :

        print(f"Subtotal: {beverage.cost()}", end="")


class Wip(Condiments):

    def cost(self) -> float:
        return self.beverage.cost() + 15 


def run(beverage: Beverage) :

        print(f"Subtotal: {beverage.cost()}", end="")



if __name__ == "__main__":
    start = True
    while(start):
        print('Select 1 Add Coffe')
        print('Select 2 Print Tiket')
        print('Select 3 Exit')
        op = input()

        if op == '1':
            tipo = input('Select type coffe: ')
            if tipo =='House Blend':
                    concret = HouseBlend()
            if tipo == 'Espresso':
                    concret = Espresso()

            agregar = True
            while(agregar):     
                c = input('What condiment ?')    
                if c =='Mocha':
                    concretda = Mocha(concret)
                if c =='Wip':
                    concretda = Wip(concret)
                if c =='Ninguno':
                    agregar=False
