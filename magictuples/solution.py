def magic_tuples(tsum, tmax):
    return ((x, y) for x in range(1, tmax) for y in range(1, tmax) if (x + y) == tsum)


if __name__ == "__main__":
    print(list(magic_tuples(5, 4)))
