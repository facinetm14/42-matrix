from src.ex13.rank import Matrix


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 12} Rank {' ' * 12}")
    print(f"{'=' * 30}")

    m1 = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])
    print(f"rank({m1}) = {m1.rank()}")
    print(f"{'' * 30}")

    m2 = Matrix([
        [1., 2., 0., 0.],
        [2., 4., 0., 0.],
        [-1., 2., 1., 1.],
    ])
    print(f"rank({m2}) = {m2.rank()}")
    print(f"{'' * 30}")

    m3 = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
        [21., 18., 7.],
    ])
    print(f"rank({m3}) = {m3.rank()}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
