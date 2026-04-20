from src.ex04.norm import Vector
from src.ex06.cross_product import cross_product


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} Cross Product {' ' * 10}")
    print(f"{'=' * 30}")

    v1 = Vector([0.0, 0.0, 1.0])
    v2 = Vector([1.0, 0.0, 0.0])
    print(f"cross({v1}, {v2}) = {cross_product(v1, v2)}")
    print(f"{'' * 30}")

    v3 = Vector([1.0, 2.0, 3.0])
    v4 = Vector([4.0, 5.0, 6.0])
    print(f"cross({v3}, {v4}) = {cross_product(v3, v4)}")
    print(f"{'' * 30}")

    v5 = Vector([4.0, 2.0, -3.0])
    v6 = Vector([-2.0, -5.0, 16.0])
    print(f"cross({v5}, {v6}) = {cross_product(v5, v6)}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
