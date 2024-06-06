"""
Problem:

Find the index of given number (target) on a sorted num array (sorted_arr)
using binary search algorithm.

target = any num
sorted_arr = sorted non-repeating num array
"""

def main():
    # sorted_arr = [1, 2, 5, 8, 10, 13, 17, 21]
    sorted_arr = []
    target = 1

    target_ind = -1

    low = 0
    high = len(sorted_arr)

    while(low < high):
        mid = low + (high - low) // 2

        if (sorted_arr[mid] < target):
            low = mid + 1
        elif (sorted_arr[mid ] > target):
            high = mid
        else:
            target_ind = mid
            break

    print(f"target: {target_ind}")

if __name__ == '__main__':
    main()
