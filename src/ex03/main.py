from src.ex03.Vector import Vector


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} Dot Product {' ' * 10}")
    print(f"{'=' * 30}")

    v1 = Vector([0.0, 0.0])
    v2 = Vector([1.0, 1.0])

    print(f"{v1} * {v2} = {v1.dot(v2)}")
    print(f"{'' * 30}")

    v3 = Vector([1.0, 1.0])
    v4 = Vector([1.0, 1.0])

    print(f"{v3} * {v4} = {v3.dot(v4)}")
    print(f"{'' * 30}")

    v5 = Vector([-1.0, 6.0])
    v6 = Vector([3.0, 2.0])

    print(f"{v5} * {v5} = {v5.dot(v6)}")
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
