"""
Most water = biggest area

Area = height x width
     = (my2 - my1) x (mx - nx) where m = point with min height, n = the other point

"""


def find_max_area_naive(height: list[int]) -> int:
    s, end = 0, len(height) - 1
    max_area = 0

    while s < end:
        t = s
        while t < end:
            distance = end - t

            min_height = min(height[t], height[end])
            area = distance * min_height

            max_area = max(max_area, area)

            t += 1
        s += 1

    return max_area


def find_points_with_max_area_two_points(height: list[int]) -> int:
    start, end = 0, len(height) - 1

    max_area = 0

    while start < end:
        distance = end - start
        min_h = min(height[start], height[end])

        area = distance * min_h
        max_area = max(max_area, area)

        if height[start] <= height[end]:
            start += 1
        else:
            end -= 1

    return max_area


def test_find_points_with_max_area():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = 49

    assert output == find_max_area_naive(height)
    assert output == find_points_with_max_area_two_points(height)


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    find_max_area_naive(height)
    find_points_with_max_area_two_points(height)
