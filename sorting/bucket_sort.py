from typing import Any, Protocol
from insertion_sort import InsertionSort
from lib.sort_order import SortOrder

class SortAlgoritm(Protocol):

    def sort(self, arr: list) -> list:
        ...


class BucketSort:

    def __init__(self,
                 stable_sorter: SortAlgoritm,
                 sort_order: SortOrder = SortOrder.ASC,
                 bucket_size: int = 10
        ) -> None:
        self.stable_sorter = stable_sorter
        self.sort_order = sort_order
        self.bucket_size = bucket_size

        self.buckets = [[] for _ in range(self.bucket_size)]

    def sort(self, arr: list) -> list:

        for val in arr:
            ind = self.get_bucket_ind(val)
            self.buckets[ind].append(val)

        for i in range(len(self.buckets)):
            self.buckets[i] = self.stable_sorter.sort(self.buckets[i])

        i = 0
        for bucket in self.buckets:
            for n in bucket:
                arr[i] = n
                i += 1

        return arr

    def get_bucket_ind(self, val: float) -> int:
        return max(int(val * self.bucket_size) - 1, 0)

    def normalize_inplace(self, arr: list) -> Any:
        max = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > max:
                max = arr[i]

        for i in range(len(arr)):
            arr[i] = arr[i] / max

        return max

    def denormalize_inplace(self, arr: list, max: Any) -> None:
        for i in range(len(arr)):
            arr[i] = int( arr[i] * max )  # Convert back to int


def main():
    sort_order_type = SortOrder.ASC
    insertion_sort = InsertionSort(sort_order_type)
    bucket_sort = BucketSort(insertion_sort, sort_order_type)

    input_arr = [5, 8, 2, 4, 6, 1, 3, 3, 3, 13, 5]
    print("Input array:", input_arr)

    normalized_val = bucket_sort.normalize_inplace(input_arr)
    output_arr = bucket_sort.sort(input_arr)
    bucket_sort.denormalize_inplace(output_arr, normalized_val)

    print("Output array:", output_arr)


if __name__ == "__main__":
    main()
