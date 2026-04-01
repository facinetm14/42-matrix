from src.ex04.norm import Vector


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} VECTORS {' ' * 10}")
    print(f"{'=' * 30}")

    v1 = Vector([0.0, 0.0, 0.0])
    print(
        f"{v1}: norm_1 = {v1.norm_1()} norm_2 = {v1.norm_2()} norm_if = {v1.norm_inf()}"
    )
    print(f"{'' * 30}")

    v2 = Vector([1.0, 2.0, 3.0])
    print(
        f"{v2}: norm_1 = {v2.norm_1()} norm_2 = {v2.norm_2()} norm_if = {v2.norm_inf()}"
    )
    print(f"{'' * 30}")

    v3 = Vector([-1.0, -2.0])
    print(
        f"{v3}: norm_1 = {v3.norm_1()} norm_2 = {v3.norm_2()} norm_if = {v3.norm_inf()}"
    )
    print(f"{'' * 30}")


if __name__ == "__main__":
    main()
