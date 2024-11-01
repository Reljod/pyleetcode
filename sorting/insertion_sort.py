from lib.sort_order import SortOrder


class InsertionSort:

    def __init__(self, sort_order: SortOrder = SortOrder.ASC):
        self.sort_order = sort_order

    def sort(self, arr: list) -> list:

        for i in range(1, len(arr)):
            for j in range(i):
                if self._compare(arr[j], arr[i]):
                    arr[j], arr[i] = arr[i], arr[j]

        return arr

    def _compare(self, u, v):
        if self.sort_order == SortOrder.ASC:
            return u > v

        return v > u


def main():
    sorter = InsertionSort()
    print("Sort Algorithm:", sorter.__class__.__name__)
    print("")

    input_arr = [5, 2, 4, 6, 1, 3]
    print("Sort by ascending:")
    print("Input Array:", input_arr)
    output_arr = sorter.sort(input_arr)
    print("Output Array:", output_arr)

    print("")

    sorter_desc = InsertionSort(sort_order=SortOrder.DESC)
    print("Sort by descending:")
    print("Input Array:", input_arr)
    output_arr = sorter_desc.sort(input_arr)
    print("Output Array:", output_arr)


if __name__ == "__main__":
    main()
