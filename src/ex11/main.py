from src.ex11.determinant import Matrix


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 9} Determinant {' ' * 9}")
    print(f"{'=' * 30}")

    m1 = Matrix([[1., -1.],
                 [-1., 1.],])
    print(f"det({m1}) = {m1.determinant()}")
    print(f"{'' * 30}")

    m2 = Matrix([[2., 0., 0.],
                 [0., 2., 0.],
                 [0., 0., 2.],])
    print(f"det({m2}) = {m2.determinant()}")
    print(f"{'' * 30}")

    m3 = Matrix([[1.0, 2.0], [2.0, 4.0]])
    print(f"det({m3}) = {m3.determinant()}")
    print(f"{'' * 30}")

    m4 = Matrix([
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
    ])
    print(f"det({m4}) = {m4.determinant()}")
    print(f"{'' * 30}")

    m5 = Matrix([
        [8.0, 5.0, -2.0, 4.0],
        [4.0, 2.5, 20.0, 4.0],
        [8.0, 5.0, 1.0, 4.0],
        [28.0, -4.0, 17.0, 1.0],
    ])
    print(f"det({m5}) = {m5.determinant()}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
