from enum import auto, Enum
from lib.sort_order import SortOrder


class PivotType(Enum):
    END = auto()
    MID = auto()
    RANDOM = auto()


class PivotHandler:

    def __init__(self, pivot_type: PivotType = PivotType.END):
        self.pivot_type = pivot_type

    def get_pivot(self, arr: list[int], low: int, high: int):
        # TODO: Implement other pivot types
        match PivotType:
            case PivotType.END:
                return high
            case _:
                return high


class QuickSort:

    def __init__(self, pivot_handler: PivotHandler, sort_order: SortOrder | None = SortOrder.ASC) -> None:
        self.pivot_handler = pivot_handler
        self.sort_order = sort_order

    def sort(self, arr: list[int], low: int = 0, high: int = -1) -> list[int]:
        high = high if high != -1 else len(arr) - 1

        if low >= high:
            return arr

        pivot_ind = self._partition(arr, low, high)
        self.sort(arr, low, pivot_ind - 1)
        self.sort(arr, pivot_ind + 1, high)

        return arr

    def _partition(self, arr: list[int], low: int, high: int) -> int:
        pivot_ind = self.pivot_handler.get_pivot(arr[low: high+1], low, high)

        j = low
        i = low - 1

        while j < high:

            if self.compare(arr[j], arr[pivot_ind]):
                i += 1
                self.swap(arr, j, i)

            j += 1

        self.swap(arr, i + 1, pivot_ind)

        return i + 1

    def swap(self, arr: list[int], u: int, v: int) -> None:
        arr[u], arr[v] = arr[v], arr[u]

    def compare(self, u: int, v: int) -> bool:
        return u < v if self.sort_order == SortOrder.ASC else v < u

def main():
    input_arr = [5, 8, 2, 4, 6, 1, 3, 3, 3, 10, 100, 5]

    pivot_handler = PivotHandler()

    sorter = QuickSort(pivot_handler)
    print("Sort by ascending:")
    print("Input Array:", input_arr)
    output_arr = sorter.sort(input_arr)
    print("Output Array:", output_arr)
    print("")

    sorter_desc = QuickSort(pivot_handler, sort_order=SortOrder.DESC)
    print("Sort by descending:")
    print("Input Array:", input_arr)
    output_arr = sorter_desc.sort(input_arr)
    print("Output Array:", output_arr)


if __name__ == "__main__":
    main()

