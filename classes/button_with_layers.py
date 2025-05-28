import pygame.display


class Button_with_layers():
    def __init__(self,buttons=[]):
        self.buttons=buttons
        self.tec_number=0
        self.max_number=len(self.buttons)
    def controller(self,events):
        if self.buttons[self.tec_number].controller(events)==1:
            if self.tec_number<self.max_number-1:
                self.tec_number+=1
            else:
                self.tec_number=0
    def risovanie(self):
        screen=pygame.display.get_surface()
        self.buttons[self.tec_number].risyem(screen)