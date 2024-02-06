import zombiedice

class Myzombie:
    def __init__(self,name):
        self.name =name

    def turn(self,gameState):
        diceRollResult=zombiedice.roll()
        brains=0
        while diceRollResult is not None:
            brains+=diceRollResult['brains']

            if brains <2:
                diceRollResult=zombiedice.roll()
            else:
                break
zombies=(zombiedice.examples.RandomCoinFlipZombie(name='Random'),\
         zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),\
         zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns',minShotguns=2), \
         zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotguns', minShotguns=1),\
         Myzombie(name='My Zombie Bot')
         )
zombiedice.runWebGui(zombies=zombies,numGames=1000)
