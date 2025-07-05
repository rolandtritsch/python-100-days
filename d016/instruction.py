"""
A class representing a turtle instruction.
"""

import typing

import turtle


class Instruction:
    @staticmethod
    def parse(instructions: str) -> list["Instruction"]:
        result: list[Instruction] = []
        for instruction in instructions.split(","):
            if instruction.startswith("F"):
                result.append(Forward(int(instruction[1:])))
            elif instruction.startswith("L"):
                result.append(Left())
            elif instruction.startswith("R"):
                result.append(Right())
            else:
                raise ValueError(f"Invalid instruction: {instruction}")
        return result

    def execute(self, turtle: "turtle.Turtle") -> None:
        pass


class Forward(Instruction):
    def __init__(self, distance: int) -> None:
        self.distance = distance

    @typing.override
    def execute(self, turtle: "turtle.Turtle") -> None:
        turtle.forward(self.distance)


class Left(Instruction):
    @typing.override
    def execute(self, turtle: "turtle.Turtle") -> None:
        turtle.left(90)


class Right(Instruction):
    @typing.override
    def execute(self, turtle: "turtle.Turtle") -> None:
        turtle.right(90)
