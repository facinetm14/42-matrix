from src.ex10.row_echelon import Matrix


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 8} ROW ECHELON Form {' ' * 8}")
    print(f"{'=' * 30}")

    m1 = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(f"{m1} row_echelon = {m1.row_echelon()}")
    print(f"{'' * 30}")

    m2 = Matrix([
        [1., 2.],
        [3., 4.],
    ])
    print(f"{m2} row_echelon = {m2.row_echelon()}")
    print(f"{'' * 30}")

    m3 = Matrix([
        [1., 2.],
        [2., 4.],
    ])
    print(f"{m3} row_echelon = {m3.row_echelon()}")
    print(f"{'' * 30}")

    m3 = Matrix([
        [1., 2., 0., 0.],
        [2., 4., 0., 0.],
        [-1., 2., 1., 1.],
    ])

    print(f"{m3} row_echelon = {m3.row_echelon()}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
