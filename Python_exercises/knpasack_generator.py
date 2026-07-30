from typing import Iterator

def knapsack(goal : int, items : list[tuple[str, int]]) -> Iterator[list[str]]:
    if goal == 0:
        yield [] # solution found
    elif not items:
        return  # out of items, no solution
    else:
        name, weight = items[0]
        remaining_items = items[1:]
        yield from knapsack(goal, remaining_items) # solutions without item0
        if weight <= goal:
            for solution in knapsack(goal - weight, remaining_items):
                yield [name] + solution

gifts = {"phone": 200, "boots": 1200, "laptop": 2200, "glasses": 50, 
"camera": 150, "jumpsuit": 2340, "headphones": 80, "fitbit": 40, 
"Hanger": 10, "pillow": 400, "hoverboard": 870, "handbag": 430}

kg500 = knapsack(500, gifts)
kg2400 = knapsack(2400, gifts)
kg4900 = knapsack(4900, gifts)
# every next yields a list[str] of gifts that fit in the suitcase

next(kg500)