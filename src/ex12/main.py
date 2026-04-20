from src.ex12.inverse import Matrix


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 11} Inverse {' ' * 11}")
    print(f"{'=' * 30}")

    m1 = Matrix([[1., 0., 0.],
                 [0., 1., 0.],
                 [0., 0., 1.],])
    print(f"inv({m1}) = {m1.inverse()}")
    print(f"{'' * 30}")

    m2 = Matrix([[2., 0., 0.],
                 [0., 2., 0.],
                 [0., 0., 2.],])
    print(f"inv({m2}) = {m2.inverse()}")
    print(f"{'' * 30}")

    m3 = Matrix([[8., 5., -2.],
                 [4., 7., 20.],
                 [7., 6., 1.],])
    print(f"inv({m3}) = {m3.inverse()}")
    print(f"{'' * 30}")

    
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
