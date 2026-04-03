from src.ex07.linear_map import Matrix
from src.ex03.Vector import Vector


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} Linear Map {' ' * 10}")
    print(f"{'=' * 30}")

    print(f"{'-' * 10} Multi-vector {'-' * 10}")
    m1 = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v1 = Vector([4.0, 2.0])

    print(f"{m1} {v1} = {m1.mul_vec(v1)}")
    print(f"{'' * 30}")

    m2 = Matrix([[2.0, 0.0], [0.0, 2.0]])
    v2 = Vector([4.0, 2.0])

    print(f"{m2} {v2} = {m2.mul_vec(v2)}")
    print(f"{'' * 30}")

    m3 = Matrix([[2.0, -2.0], [-2.0, 2.0]])
    v3 = Vector([4.0, 2.0])

    print(f"{m3} {v3} = {m3.mul_vec(v3)}")
    print(f"{'' * 30}")

    m3 = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v3 = Vector([4.0, 2.0])

    print(f"{m3} {v3} = {m3.mul_vec(v3)}")
    print(f"{'' * 30}")

    print(f"{'-' * 10} Multi-matrix {'-' * 10}")
    m4 = Matrix([[1.0, 0.0], [0.0, 1.0]])
    m5 = Matrix(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ]
    )

    print(f"{m4} {m5} = {m4.mul_mat(m5)}")
    print(f"{'' * 30}")

    m6 = Matrix([[1.0, 0.0], [0.0, 1.0]])
    m7 = Matrix([[2.0, 1.0], [4.0, 2.0]])

    print(f"{m6} {m7} = {m6.mul_mat(m7)}")
    print(f"{'' * 30}")

    m8 = Matrix([[3.0, -5.0], [6.0, 8.0]])
    m9 = Matrix(
        [
            [2.0, 1.0],
            [4.0, 2.0],
        ]
    )

    print(f"{m8} {m9} = {m8.mul_mat(m9)}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
