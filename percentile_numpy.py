from numpy import percentile, array
from functools import partial


if __name__ == "__main__":
    # convert the list of numeric strings to numpy.array of integers
    value_list = array(input().split(), dtype=int)

    # create a function to get the twentieth percentile
    twentieth_percentile = partial(percentile, q=20)

    print(twentieth_percentile(value_list))
