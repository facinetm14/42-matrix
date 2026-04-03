from src.ex09.transpose import Matrix


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} transpose {' ' * 10}")
    print(f"{'=' * 30}")

    m1 = Matrix([[1., 0.],
                 [0., 1.]])
    print(f"{m1} transpose = {m1.transpose()}")
    print(f"{'' * 30}")

    m2 = Matrix([[2., -5., 0.],
                 [4., 3., 7.],
                 [-2., 3., 4.]])
    print(f"{m2} transpose = {m2.transpose()}")
    print(f"{'' * 30}")

    m3 = Matrix([[-2., -8., 4.],
                 [1., -23., 4.],
                 [0., 6., 4.],])
    print(f"{m3} transpose = {m3.transpose()}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
