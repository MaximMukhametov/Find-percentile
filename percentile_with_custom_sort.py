from typing import Optional


def search_percentile(array: list, index: int) -> Optional[int]:
    """
    Looks for the approximate percentile in the data array.
    This is something like a stripped-down version of quicksort, because
    there is no need to honestly sort the whole array to find the percentile
    """
    if len(array) == 0:
        return None
    else:
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

        if index == len(below_values) or (
                len(below_values) < index < (
                len(below_values) + len(equal_values))):
            return array[index]

        elif above_values and index > len(below_values):
            index = index - len(below_values) - len(equal_values)
            return search_percentile(above_values, index)

        return search_percentile(below_values, index)


if __name__ == "__main__":
    value_list = input().split()
    percent = 0.2
    target_index = round(len(value_list) * percent)
    print(search_percentile(value_list, target_index))
