directions = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S",
              "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]


def get_direction(deg: int) -> str:
    i, num = map(int, divmod(deg / 112.5, 2))
    if num != 1:
        return directions[i - 1]
    else:
        return directions[i]


def main():
    deg, dis = map(int, input().split())
    print(divmod(deg, 112.5))
    print(get_direction(deg))


if __name__ == '__main__':
    main()
