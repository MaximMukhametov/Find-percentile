from typing import Optional, Union

from numpy import array, percentile as numpy_percentile


def percentile(data_set: list,
               percent: Union[int, float]) -> Optional[float]:
    """Find the percentile of an array of values."""
    if not data_set:
        return None
    data_set = array(data_set, dtype=int)
    return numpy_percentile(data_set, percent)


if __name__ == "__main__":
    value_list = input().split()
    print(percentile(value_list, 20))
