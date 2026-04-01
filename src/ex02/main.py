from src.ex00.Vector import Vector
from src.ex00.Matrix import Matrix

from src.ex02.linear_interpolation import lerp


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} Linear Interpolation {' ' * 10}")
    print(f"{'=' * 30}")

    u1 = 0.0
    v1 = 1.0
    t1 = 0.0
    print(f"lerp({u1}, {v1}, {t1}) = {lerp(u1, v1, t1)}")
    print(f"{'' * 30}")

    u2 = 0.0
    v2 = 1.0
    t2 = 1.0
    print(f"lerp({u2}, {v2}, {t2}) = {lerp(u2, v2, t2)}")
    print(f"{'' * 30}")

    u3 = 0.0
    v3 = 1.0
    t3 = 0.5
    print(f"lerp({u3}, {v3}, {t3}) = {lerp(u3, v3, t3)}")
    print(f"{'' * 30}")

    u4 = 21.0
    v4 = 42.0
    t4 = 0.3
    print(f"lerp({u4}, {v4}, {t4}) = {lerp(u4, v4, t4)}")
    print(f"{'' * 30}")

    u5 = Vector([2.0, 1.0])
    v5 = Vector([4.0, 2.0])
    t5 = 0.3

    print(f"lerp({u5}, {v5}, {t5}) = {lerp(u5, v5, t5)}")
    print(f"{'' * 30}")

    u6 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    v6 = u6.scl(10.0)
    t6 = 0.5

    print(f"lerp({u6}, {v6}, {t6}) = {lerp(u6, v6, t6)}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
