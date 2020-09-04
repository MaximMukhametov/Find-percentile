from typing import Optional


def search_percentile(array: list,
                      index: int = None,
                      percent: float = None) -> Optional[int]:
    """
    Looks for the approximate percentile in the data array.
    This is something like a stripped-down version of quicksort, because
    there is no need to honestly sort the whole array to find the percentile.
    """
    if not array:
        return None
    else:
        # finds a rounded index equal to a percentage of the length of an array
        index = round(len(value_list) * percent) if percent else index
        below_values = []
        above_values = []
        equal_values = []
        for n in array:
            n = int(n)
            if n < int(array[index]):
                below_values.append(n)
            elif n > int(array[index]):
                above_values.append(n)
            else:
                equal_values.append(n)

        below_values_length = len(below_values)

        if index == below_values_length or (
                below_values_length < index < (
                below_values_length + len(equal_values))):
            return array[index]

        elif above_values and index > below_values_length:
            # discard the left side of the array and index recalculation
            index = index - below_values_length - len(equal_values)
            return search_percentile(above_values, index)

        # discard the right side of the array
        return search_percentile(below_values, index)


if __name__ == "__main__":
    value_list = input().split()
    print(search_percentile(value_list, percent=0.2))
