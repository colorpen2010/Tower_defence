import time

import pygame.time


class Time():
    def __init__(self):
        pass

    def create_timer(self,miliseconds,event_number):
        pygame.time.set_timer(event_number,miliseconds)

    def timers_change(self,procent):
        pass