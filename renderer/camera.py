from dataclasses import dataclass

class Camera:

    def __init__(self, position: list[float], eulers: list[int]) -> None:
        self.postion = position
        self.eulers = eulers

