import math
from typing import Optional


def percentile(array: list, percent: float) -> Optional[float]:
    """Find the percentile of an array of values."""
    if len(array) == 0:
        return None

    array.sort()
    exact_index = (len(array) - 1) * percent
    ceil_index = math.ceil(exact_index)
    floor_index = math.floor(exact_index)

    if floor_index == ceil_index:
        return int(array[int(exact_index)])

    # interpolates values against an exact index
    below_part = int(array[int(floor_index)]) * (ceil_index - exact_index)
    above_part = int(array[int(ceil_index)]) * (exact_index - floor_index)

    return below_part + above_part


if __name__ == "__main__":
    value_list = [int(item) for item in input().split()]
    print(percentile(value_list, 0.2))
