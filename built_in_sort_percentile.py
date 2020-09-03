from typing import Optional


def search_percentile(array: list, percent: float) -> Optional[int]:
    """Looks for the approximate percentile in the data array."""
    if not array:
        return None
    array.sort()
    target_index = round(len(array) * percent)
    return array[target_index]


if __name__ == "__main__":
    value_list = [int(item) for item in input().split()]
    print(search_percentile(value_list, 0.2))
