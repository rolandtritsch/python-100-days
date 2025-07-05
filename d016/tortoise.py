"""
Makes the turtle move.

The instructions are a string of characters representing the moves
the turtle should make.

Each character corresponds to a specific move:

- 'F<N': Move forward by N units
- 'L': Turn left by 90 degrees
- 'R': Turn right by 90 degrees

The moves are separated by commas.

For example, "F10,L,R,F5" means move forward 10 units, turn left,
turn right, and then move forward 5 units.
"""

import argparse
import sys
import turtle

# Use absolute import to avoid mypy issues
import d016.instruction as instruction
import structlog

import util.logging

util.logging.init()
logger = structlog.get_logger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a turtle race")
    parser.add_argument("instructions", type=str, help="The moves for the turtle")
    return parser.parse_args()


def process_args(args: argparse.Namespace) -> list[instruction.Instruction]:
    return instruction.Instruction.parse(args.instructions)


def main() -> None:
    args = parse_args()
    instructions = process_args(args)
    logger.info(f"Parsed instructions: {instructions}")

    t = turtle.Turtle()
    t.shape("turtle")
    t.color("coral")

    for i in instructions:
        i.execute(t)

    t.screen.mainloop()

    sys.exit(0)


if __name__ == "__main__":
    main()
