class Battleship():

    def __init__(self,name):
        self.location = []
        self.name = name
        self.hits = []


    def placeShip(self, enemy):
        choice = input('where would you like to place your ship?')
        if choice not in enemy.location:
            self.location.append(choice)
            print('done and done')
        else:
            print('there are rocks there')
            self.placeShip(enemy)

    def battle(self,enemy):
            where = input('where do you want to hit?')
            print(self.name)
            if where in enemy.location:
                print('hit')
                enemy.hits.append(where)
                enemy.location.remove(where)
            else:
                enemy.battle(self)

    def printBoard(self,enemy):
        print(self.hits)
        print(enemy.hits)


england = Battleship('england')
france = Battleship('france')
england.placeShip(france)
france.placeShip(england)
england.battle(france)
