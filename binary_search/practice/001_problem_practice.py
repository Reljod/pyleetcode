from typing import Any

def find_target_ind(input_arr: list[Any], target: Any) -> int:
    input_arr_len = len(input_arr)

    left_idx = 0
    right_idx = input_arr_len - 1

    while left_idx <= right_idx:
        mid_idx = (right_idx + left_idx) // 2

        mid_value = input_arr[mid_idx]

        if target < mid_value:
            right_idx = mid_idx
        elif target > mid_value:
            left_idx = mid_idx + 1
        else:
            # target == mid_value
            return mid_idx

    return -1

def main():
    input_arr = [4, 5, 10, 13, 14, 22, 23]
    target = 22

    target_ind = find_target_ind(input_arr, target)
    print(f"The target is {'Missing' if target_ind == -1 else target_ind}")

if __name__ == "__main__":
     main()
