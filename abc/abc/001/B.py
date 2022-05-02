def convert_to_visible(distance: int) -> int:
    """距離を視程へ変換する

    Args:
        distance (int): 距離

    Returns:
        int: 視程の値(通報式)
    """
    if distance < 0.1:
        return 0
    if 0.1 <= distance <= 5:
        return distance * 10
    if 6 <= distance <= 30:
        return distance + 50
    if 35 <= distance <= 70:
        return distance + 80
    if 70 < distance:
        return 89


def main():
    distance = int(input()) / 1000
    print(f"{convert_to_visible(distance):02}")


if __name__ == '__main__':
    main()
