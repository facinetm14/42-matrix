from src.ex00.Vector import Vector
from src.ex01.linear_combination import linear_combination


def main():

    print(f"{'=' * 30}")
    print(f"{' ' * 10} Linear combination {' ' * 10}")
    print(f"{'=' * 30}")

    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])
    e_scalars = [10., -2., 0.5]
    
    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    v_scalars = [10., -2]
    
    print(f"[{e1}, {e2}, {e3}] {e_scalars} = {linear_combination([e1, e2, e3], e_scalars)}")
    print(f"{'' * 30}")

    print(f"[{v1}, {v2}] {e_scalars} = {linear_combination([v1, v2], v_scalars)}")
    print(f"{'' * 30}")




if __name__ == "__main__":
    main()
