
class Beverage():

    def cost(self) -> float:
        pass


class Espresso(Beverage):

    def cost(self) -> float:
        return 50.99

class  HouseBlend(Beverage):

    def cost(self) -> float:
        return 50.99



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
        return self.beverage.cost() + 7.2 


def run(beverage: Beverage) :

        print(f"Subtotal: {beverage.cost()}", end="")


class Wip(Condiments):

    def cost(self) -> float:
        return self.beverage.cost() + 9.3 


def run(beverage: Beverage) :

        return beverage.cost()



if __name__ == "__main__":
    start = True
    while(start):
        print('Select 1 Add Coffe')
        print('Select 2 Print Tiket')
        print('Select 3 Exit')
        op = input("ingrese")
        cont = 0
        cont = float(cont)


        if op == '1':
            print('House Blend or Espresso')
            tipo = input('Select type coffe: ')
            if tipo =='House Blend':
                concret = HouseBlend()
            if tipo == 'Espresso':
                concret = Espresso()

            agregar = True
            while(agregar):     
                d = input('Add condiment ?') 
                if  d ==  'Yes':
                    print('Wip or Mocha')
                    c = input('What condiment ?') 
                    if c =='Mocha':
                        cont += float(Mocha(concret))
                    if c =='Wip':
                        cont += Wip(cont)
                    if c =='Salir':
                        agregar=False

                if d == 'No':
                    cont += run(concret)
                    agregar=False
                

        if op =='2':
            print(cont)
        

        if op =='3':
            start = False
