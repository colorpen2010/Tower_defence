import pygame

import kakoito_resizer

fontik=pygame.font.SysFont('Arial',25,True)
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
        self.outmoney=kakoito_resizer.sheti(self.money)
        self.outmoney = fontik.render('$' + str(self.outmoney), True, [0, 0, 0])
    def _render(self):
        self.outmoney=fontik.render('$' + str(kakoito_resizer.sheti(self.money)), True, [0, 0, 0])

    def otnimanie(self,zena):
        self.money-=zena
        self._render()



    def set_money(self,amount):
        self.money=amount
        self._render()


    def grafiti(self,x,y):
        screen=pygame.display.get_surface()
        screen.blit(self.outmoney, [x, y])