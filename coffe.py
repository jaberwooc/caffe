class Beverage():

    def cost(self) -> float:
        pass


class Espresso(Beverage):

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





if __name__ == "__main__":
    concret = Espresso()
    concretda = Mocha(concret)
    start = True
    while(start):
        if c =='Mocha':
            run(concretda)
        if c =='Wip':
            run(concretda)
