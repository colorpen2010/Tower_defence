import pygame.transform

from classes import animator


class Rotating(animator.Animator):
    def __init__(self,left_pack=None,right_pack=None,up_pack=None,down_pack=None):
        assert left_pack is not None or right_pack is not None, "cocacola ili babaji"
        assert up_pack is not None or down_pack is not None, "babaji ili fortinaiti"
        if left_pack is None:
            pygame.transform.flip(right_pack,1,0)
