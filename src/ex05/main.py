from src.ex04.norm import Vector
from src.ex05.cosine import angle_cos


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} Cosine {' ' * 10}")
    print(f"{'=' * 30}")

    v1 = Vector([1.0, 0.0])
    v2 = Vector([1.0, 0.0])
    print(f"cos({v1}, {v2}) = {angle_cos(v1, v2)}")
    print(f"{'' * 30}")

    v3 = Vector([1.0, 0.0])
    v4 = Vector([0.0, 1.0])
    print(f"cos({v3}, {v4}) = {angle_cos(v3, v4)}")
    print(f"{'' * 30}")

    v5 = Vector([-1.0, 1.0])
    v6 = Vector([1.0, -1.0])
    print(f"cos({v5}, {v6}) = {angle_cos(v5, v6)}")
    print(f"{'' * 30}")

    v7 = Vector([2.0, 1.0])
    v8 = Vector([4.0, 2.0])
    print(f"cos({v7}, {v8}) = {angle_cos(v7, v8)}")
    print(f"{'' * 30}")

    v9 = Vector([1.0, 2.0, 3.0])
    v10 = Vector([4.0, 5.0, 6.0])
    print(f"cos({v9}, {v10}) = {angle_cos(v9, v10)}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
