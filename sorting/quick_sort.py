from enum import Enum, auto


class SortOrder(Enum):
    ASC = auto()
    DESC = auto()


class QuickSort:

    def __init__(self, sort_order: SortOrder | None = SortOrder.ASC) -> None:
        self.sort_order = sort_order

    def sort(self, arr: list[int], pivot_ind = -1) -> list[int]:
        if pivot_ind >= len(arr) and pivot_ind != -1:
            raise ValueError(f"Pivot index {pivot_ind} not allowed from arr of len {len(arr)}")

        pivot_ind = pivot_ind if pivot_ind >= 0 else len(arr) + pivot_ind

        if len(arr) <= 1:
            return arr

        i, j = -1, 0
        while j < pivot_ind:
            if self._compare(arr[j], arr[pivot_ind]):
                i += 1
                arr[j], arr[i] = arr[i], arr[j]

            j += 1

            if j == pivot_ind:
                i += 1
                arr[pivot_ind], arr[i] = arr[i], arr[pivot_ind]

        return self.sort(arr[:i], i-1) + [arr[i]] + self.sort(arr[i+1:], len(arr[i+1:]) - 1)

    def _compare(self, u: int, v: int) -> bool:
        return u < v if self.sort_order == SortOrder.ASC else u > v


def main():
    input_arr = [5, 8, 2, 4, 6, 1, 3, 3, 3, 10, 100]

    sorter = QuickSort()
    print("Sort by ascending:")
    print("Input Array:", input_arr)
    output_arr = sorter.sort(input_arr)
    print("Output Array:", output_arr)
    print("")

    sorter_desc = QuickSort(sort_order=SortOrder.DESC)
    print("Sort by descending:")
    print("Input Array:", input_arr)
    output_arr = sorter_desc.sort(input_arr)
    print("Output Array:", output_arr)


if __name__ == "__main__":
    main()
