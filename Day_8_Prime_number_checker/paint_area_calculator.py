import math

test_h = int(input())
test_w = int(input())
coverage = 5


def paint_calc(height, width, cover):
    no_of_cans = height * width / cover
    round_cand = math.ceil(no_of_cans)
    print(f"You'll need {round_cand} cans of paint.")


paint_calc(height=test_h, width=test_w, cover=coverage)
