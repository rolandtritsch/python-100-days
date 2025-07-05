"""
Do a turtle race.

Pass the number of turtles to race as an argument.
"""

import argparse
import random
import sys
import time
import tkinter.messagebox
import turtle
import typing

import structlog

import util.logging

util.logging.init()
logger = structlog.get_logger(__name__)


def done(turtles: dict[str, turtle.Turtle], screen: typing.Any) -> bool:
    return any(t.xcor() >= screen.canvwidth / 2 for t in turtles.values())


def winner(turtles: dict[str, turtle.Turtle]) -> str:
    return max(turtles, key=lambda k: turtles[k].xcor())


def main() -> None:
    parser = argparse.ArgumentParser(description="Do a turtle race.")
    parser.add_argument("num_turtles", type=int, help="Number of turtles to race")
    args = parser.parse_args()

    if args.num_turtles not in [1, 10]:
        logger.error("Number of turtles must be in [1, 10]")
        sys.exit(1)

    s = turtle.Screen()
    s.title("Turtle Race")
    s.colormode(255)
    spacing = s.canvheight / (args.num_turtles + 1)

    turtles = {}
    for n in range(args.num_turtles):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        )
        t.teleport(-s.canvwidth, -s.canvheight / 2 + spacing * (n + 1))
        turtles[f"turtle_{n}"] = t

    logger.info(f"Turtles initialized: {turtles}")

    while not done(turtles, s):
        for t in turtles.values():
            t.forward(random.randint(1, 100))
        time.sleep(0.1)

    tkinter.messagebox.showinfo(title="The winner is:", message=winner(turtles))

    s.exitonclick()

    sys.exit(0)


if __name__ == "__main__":
    main()
