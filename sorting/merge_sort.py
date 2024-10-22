from enum import Enum, auto


class SortOrder(Enum):
    ASC = auto()
    DESC = auto()


class MergeSort:

    def __init__(self, sort_order: SortOrder | None = SortOrder.ASC) -> None:
        self.sort_order = sort_order

    def sort(self, arr: list[int]) -> list[int]:
        return self._merge_sort(arr)

    def _merge_sort(self, arr: list[int]) -> list[int]:
        arr_len = len(arr)

        if arr_len == 1:
            return arr

        arr1 = arr[:(arr_len//2)]
        arr2 = arr[arr_len//2:]

        return self._merge(self._merge_sort(arr1), self._merge_sort(arr2))

    def _merge(self, u: list[int], v: list[int]) -> list[int]:
        new_arr = []
        i, j = 0, 0
        while i < len(u) or j < len(v):

            # If all elements of 1st array is filled
            # then fill-in the rest of 2nd array
            if i >= len(u):
                new_arr.extend(v[j:])
                break

            # If all elements of 2nd array is filled
            # then fill-in the rest of 1st array
            if j >= len(v):
                new_arr.extend(u[i:])
                break

            if self._compare(u[i], v[j]):
                new_arr.append(u[i])
                i += 1
            else:
                new_arr.append(v[j])
                j += 1

        return new_arr

    def _compare(self, u: int, v: int) -> bool:
        if self.sort_order == SortOrder.ASC:
            return u <= v

        return v <= u


def main():
    sorter = MergeSort()
    print("Sort Algorithm:", sorter.__class__.__name__)
    print("")

    input_arr = [5, 8, 2, 4, 6, 1, 3, 3, 3, 10, 100]
    print("Sort by ascending:")
    print("Input Array:", input_arr)
    output_arr = sorter.sort(input_arr)
    print("Output Array:", output_arr)

    print("")

    sorter_desc = MergeSort(sort_order=SortOrder.DESC)
    print("Sort by descending:")
    print("Input Array:", input_arr)
    output_arr = sorter_desc.sort(input_arr)
    print("Output Array:", output_arr)


if __name__ == "__main__":
    main()
