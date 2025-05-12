
import pygame.time


class Time():
    def __init__(self):
        self.timer_events=[]

    def create_timer(self,event_number,miliseconds):
        pygame.time.set_timer(event_number,miliseconds)
        self.timer_events.append([event_number,miliseconds])


    def timers_change(self,procent):
        for event in self.timer_events:
            procent_result=procent/100*event[1]
            self.timer = pygame.time.set_timer(event[0], int(procent_result))


timer_worker=Time()