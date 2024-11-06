import pygame
fontik=pygame.font.SysFont('Arial',50,True)
wallet=None

def get_wallet(money):
    global wallet
    if wallet!=None:
        return wallet
    else:
        wallet=Wallet(money)
        return wallet

class Wallet():
    def __init__(self,wallett):
        wallet=wallett
        self.money=wallet
        self.outmoney=fontik.render('$' + str(self.money), True, [0, 0, 0])

    def otnimanie(self,zena):
            self.money-=zena
            self.outmoney=fontik.render('$' + str(self.money), True, [0, 0, 0])


    def grafiti(self,x,y):
        screen=pygame.display.get_surface()
        screen.blit(self.outmoney, [x, y])