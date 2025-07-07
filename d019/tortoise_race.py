"""
Do a turtle race.

Pass the number of turtles to race as an argument.
"""

import argparse
import random
import sys
import time
import tkinter.messagebox as messagebox
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


def box_it(screen: turtle.Screen):
    t = turtle.Turtle()
    t.color("black")
    t.pen(fillcolor="black", pencolor="red", pensize=10)
    t.teleport(-screen.canvwidth / 2, screen.canvheight / 2)
    t.goto(-screen.canvwidth / 2, -screen.canvheight / 2)
    t.goto(screen.canvwidth / 2, -screen.canvheight / 2)
    t.goto(screen.canvwidth / 2, screen.canvheight / 2)
    t.goto(-screen.canvwidth / 2, screen.canvheight / 2)


def init_turtles(num_turtles: int, screen: turtle.Screen) -> dict[str, turtle.Turtle]:
    spacing = screen.canvheight / (num_turtles + 1)

    turtles = {}
    screen.colormode(255)
    for n in range(num_turtles):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        )
        t.teleport(-screen.canvwidth / 2, -screen.canvheight / 2 + spacing * (n + 1))
        turtles[f"turtle_{n}"] = t

    return turtles


def run_race(turtles: dict[str, turtle.Turtle], screen: turtle.Screen) -> None:
    while not done(turtles, screen):
        for t in turtles.values():
            t.forward(random.randint(1, 100))
        time.sleep(0.1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Turtle Race")
    parser.add_argument(
        "num_turtles", type=int, help="Number of turtles to race",
    )

    args = parser.parse_args()

    if args.num_turtles not in [1, 10]:
        logger.error("Number of turtles must be in [1, 10]")
        sys.exit(1)

    return args


def main() -> None:
    args = parse_args()

    screen = turtle.Screen()
    screen.title("Turtle Race")

    box_it(screen)

    turtles = init_turtles(args.num_turtles, screen)
    logger.info(f"Turtles initialized: {turtles}")

    run_race(turtles, screen)

    messagebox.showinfo(title="The winner is:", message=winner(turtles))

    screen.exitonclick()

    sys.exit(0)


if __name__ == "__main__":
    main()
