from src.ex08.trace import Matrix


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} Trace {' ' * 10}")
    print(f"{'=' * 30}")

    m1 = Matrix([[1., 0.],
                 [0., 1.]])
    print(f"{m1} trace = {m1.trace()}")
    print(f"{'' * 30}")

    m2 = Matrix([[2., -5., 0.],
                 [4., 3., 7.],
                 [-2., 3., 4.]])
    print(f"{m2} trace = {m2.trace()}")
    print(f"{'' * 30}")

    m3 = Matrix([[-2., -8., 4.],
                 [1., -23., 4.],
                 [0., 6., 4.],])
    print(f"{m3} trace = {m3.trace()}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
