from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    return raw_puzzle_in.split("\n")


def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    # Create a nested list??
    # Depth == depth in list
    # Root == step 1

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{puzzle}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{puzzle}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(tst_input)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = transform_input(tst_input)
    solve_puzzle_2(transfrmd_inp_p2)