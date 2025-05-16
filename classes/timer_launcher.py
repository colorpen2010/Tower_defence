
import pygame.time


class Time():
    def __init__(self):
        self.timer_events=[]
        self.procent=100

    def create_timer(self,event_number,miliseconds):
        self.shoti(event_number, miliseconds)
        self.timer_events.append([event_number,miliseconds])

    def timers_change(self,procent):
        self.procent=procent
        for event in self.timer_events:
            self.shoti(event[0],event[1])

    def delete_timer(self,event_number):
        pygame.time.set_timer(event_number,0)
        for o in self.timer_events:
            if o[0]==event_number:
                self.timer_events.remove(o)


    def shoti(self,event_number,miliseconds):
        procent_result = self.procent / 100 * miliseconds
        pygame.time.set_timer(event_number,0)
        pygame.time.set_timer(event_number, int(procent_result))


timer_worker=Time()